from fastapi import FastAPI, File, UploadFile
import shutil
import uuid
import subprocess
import sys
from pathlib import Path
import ollama

app = FastAPI()
UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

# Carregar o modelo LLaMA (ajuste o caminho do modelo conforme necessário)
llm = Llama(model_path="models/llama-7b.gguf")  # Ajuste o nome do modelo

def save_image(file: UploadFile) -> Path:
    file_extension = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = UPLOAD_FOLDER / filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file_path

@app.post("/process_image/")
async def process_image(file: UploadFile = File(...)):
    image_path = save_image(file)

    process = subprocess.run(
        [sys.executable, "main.py", str(image_path)], capture_output=True, text=True
    )

    if process.returncode != 0:
        return {"error": "Erro ao processar a imagem", "details": process.stderr}

    # Enviar a saída do `main.py` para o LLaMA
    prompt = f"O que significa este resultado?\n{process.stdout.strip()}"
    response = llm(prompt, max_tokens=100)  # Ajuste os tokens conforme necessário

    return {"corrected_colors": process.stdout.strip(), "llama_response": response["choices"][0]["text"]}

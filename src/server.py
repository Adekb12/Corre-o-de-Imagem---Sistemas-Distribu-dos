from fastapi import FastAPI, File, UploadFile
import shutil
import uuid
import subprocess
import sys
import json
from pathlib import Path
import ollama
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

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
        [sys.executable, "main.py", str(image_path)], 
        capture_output=True, 
        text=True
    )

    if process.returncode != 0:
        return {"error": "Erro ao processar a imagem", "details": process.stderr}

    try:
        corrected_colors = json.loads(process.stdout.strip())
    except json.JSONDecodeError:
        return {"error": "Erro ao processar os dados", "details": process.stdout.strip()}

    prompt = f"Qual o significado das cores corrigidas? {corrected_colors}"
    client = ollama.Client(host="http://ollama:11434")
    response = client.generate(model="llama3", prompt=prompt)

    return {"corrected_colors": corrected_colors, "llama_response": response["response"]}

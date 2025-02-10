import os
import sys
from roboflow import Roboflow
from PIL import Image
from contextlib import contextmanager

API_KEY = "npZkALCtAevgZlitajPx"
MODEL_NAME = "detect_color_rectangle"
VERSION = 1

@contextmanager
def suppress_stdout():
    """Redireciona a saída padrão para suprimir mensagens do Roboflow."""
    with open(os.devnull, "w") as fnull:
        old_stdout = sys.stdout
        sys.stdout = fnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

try:
    with suppress_stdout():
        rf = Roboflow(api_key=API_KEY)
        project = rf.workspace().project(MODEL_NAME)
        model = project.version(VERSION).model
except Exception as e:
    print(f"Erro ao conectar ao Roboflow: {e}")
    exit()

def detect_and_crop_palette(image_path):
    """Detecta e recorta a paleta de cores na imagem usando Roboflow."""
    try:
        prediction = model.predict(image_path, confidence=40, overlap=30)
        predictions_data = prediction.json()

        if not predictions_data['predictions']:
            print(f"Nenhuma paleta de cores detectada em {image_path}")
            return None

        img = Image.open(image_path)
        cropped_palettes = []

        for pred in predictions_data['predictions']:
            x, y, width, height = pred['x'], pred['y'], pred['width'], pred['height']

            left, top = int(x - width / 2), int(y - height / 2)
            right, bottom = int(x + width / 2), int(y + height / 2)

            cropped_palette = img.crop((left, top, right, bottom))
            cropped_palettes.append(cropped_palette)

        return cropped_palettes

    except Exception as e:
        print(f"Erro ao detectar e recortar a paleta de cores: {e}")
        return None

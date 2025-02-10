import os
import sys
from roboflow import Roboflow
from PIL import Image, ImageDraw
from contextlib import contextmanager

API_KEY = "npZkALCtAevgZlitajPx"
MODEL_NAME = "detect_color_circle"
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

def detect_and_crop_circle(image_path):
    """Detecta e recorta o círculo na imagem usando Roboflow."""
    try:
        prediction = model.predict(image_path, confidence=40, overlap=30)
        predictions_data = prediction.json()

        if not predictions_data['predictions']:
            print(f"Nenhum círculo detectado em {image_path}")
            return None

        img = Image.open(image_path).convert("RGBA")
        cropped_images = []

        for pred in predictions_data['predictions']:
            x, y, diameter = pred['x'], pred['y'], pred['width']

            mask = Image.new("L", img.size, 0)
            draw = ImageDraw.Draw(mask)
            left, top = int(x - diameter / 2), int(y - diameter / 2)
            right, bottom = int(x + diameter / 2), int(y + diameter / 2)
            draw.ellipse((left, top, right, bottom), fill=255)

            result = Image.new("RGBA", img.size, (0, 0, 0, 0))
            result.paste(img, (0, 0), mask=mask)

            cropped_img = result.crop((left, top, right, bottom))
            cropped_images.append(cropped_img.convert("RGB"))

        return cropped_images

    except Exception as e:
        print(f"Erro ao detectar e recortar o círculo: {e}")
        return None

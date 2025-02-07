import json
from roboflow import Roboflow
from PIL import Image

API_KEY = "npZkALCtAevgZlitajPx"
MODEL_NAME = "detect_color_rectangle"
VERSION = 1

try:
    rf = Roboflow(api_key=API_KEY)
    project = rf.workspace().project(MODEL_NAME)
    model = project.version(VERSION).model
except Exception as e:
    print(f"Erro ao conectar ao Roboflow: {e}")
    exit()

def detect_and_crop_palette(image_path):
    try:
        prediction = model.predict(image_path, confidence=40, overlap=30)
        predictions_data = prediction.json()

        if not predictions_data['predictions']:
            print(f"Nenhuma paleta de cores detectada em {image_path}")
            return None

        img = Image.open(image_path)
        cropped_palettes = []

        for pred in predictions_data['predictions']:
            x = pred['x']
            y = pred['y']
            width = pred['width']
            height = pred['height']

            left = int(x - width / 2)
            top = int(y - height / 2)
            right = int(x + width / 2)
            bottom = int(y + height / 2)

            cropped_palette = img.crop((left, top, right, bottom))
            cropped_palettes.append(cropped_palette)

        return cropped_palettes

    except Exception as e:
        print(f"Erro ao detectar e recortar a paleta de cores: {e}")
        return None

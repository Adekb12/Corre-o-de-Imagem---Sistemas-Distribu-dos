import os
import json
from roboflow import Roboflow
from PIL import Image, ImageDraw

API_KEY = "npZkALCtAevgZlitajPx"
MODEL_NAME = "detect_color_circle"
VERSION = 1

try:
    rf = Roboflow(api_key=API_KEY)
    project = rf.workspace().project(MODEL_NAME)
    model = project.version(VERSION).model
except Exception as e:
    print(f"Erro ao conectar ao Roboflow: {e}")
    exit()

def detect_and_crop_circle(image_path):
    try:
        prediction = model.predict(image_path, confidence=40, overlap=30)
        predictions_data = prediction.json()

        if not predictions_data['predictions']:
            print(f"Nenhum círculo detectado em {image_path}")
            return None

        img = Image.open(image_path).convert("RGBA")
        cropped_images = []

        for pred in predictions_data['predictions']:
            x = pred['x']
            y = pred['y']
            diameter = pred['width']

            mask = Image.new("L", img.size, 0)
            draw = ImageDraw.Draw(mask)
            left = int(x - diameter / 2)
            top = int(y - diameter / 2)
            right = int(x + diameter / 2)
            bottom = int(y + diameter / 2)
            draw.ellipse((left, top, right, bottom), fill=255)

            result = Image.new("RGBA", img.size, (0, 0, 0, 0))
            result.paste(img, (0, 0), mask=mask)

            cropped_img = result.crop((left, top, right, bottom))
            cropped_images.append(cropped_img.convert("RGB"))
        return cropped_images

    except Exception as e:
        print(f"Erro ao detectar e recortar o círculo: {e}")
        return None

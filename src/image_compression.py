from PIL import Image
import io

def compress_image(image_path, quality=60):
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGB")
            img_bytes = io.BytesIO()
            img.save(img_bytes, format="JPEG", quality=quality)
            img_bytes.seek(0)
            return Image.open(img_bytes)
    except Exception as e:
        print(f"Erro ao compactar {image_path}: {e}")
        return None

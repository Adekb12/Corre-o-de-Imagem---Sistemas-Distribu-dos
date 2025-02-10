import argparse
from correct_color import color_correction
from image_compression import compress_image
from circle_detection import detect_and_crop_circle
from palette_detection import detect_and_crop_palette
from circle_color import get_circle_color
from palette_color import get_palette_color
from display_color import display_color

def main(image_path):
    compressed_image = compress_image(image_path)
    if compressed_image is None:
        print("Erro ao compactar a imagem.")
        return None

    cropped_circle = detect_and_crop_circle(image_path)
    cropped_palette = detect_and_crop_palette(image_path)

    if not cropped_circle or not cropped_palette:
        print("Círculo ou paleta de cores não detectados.")
        return None

    corrected_colors = []

    for circle_img, palette_img in zip(cropped_circle, cropped_palette):
        circle_color = get_circle_color(circle_img)
        camera_colors = get_palette_color(palette_img)
        corrected_color = color_correction(camera_colors, circle_color)
        corrected_colors.append(corrected_color.tolist())

    print(corrected_colors)

    for color in corrected_colors:
        display_color(color)

    return corrected_colors

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Corrigir cores de uma imagem.")
    parser.add_argument("image_path", type=str, help="Caminho para a imagem a ser processada")
    args = parser.parse_args()
    
    main(args.image_path)

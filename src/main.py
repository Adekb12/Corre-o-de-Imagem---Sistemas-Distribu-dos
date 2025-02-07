import numpy as np
from color_correction import correct_color  # Importa a função de correção de cores

def main(image_path):
    """
    Função principal que processa a imagem e retorna a cor corrigida.
    """
    # 1. Receber a imagem (simulado com um caminho de arquivo)
    print(f"Processando imagem ...")

    # 2. Enviar a imagem para os modelos
    circle = detect_circle(image_path)  # Codigo que detecta o círculo
    palette = extract_palette(image_path)  # Codigo que extrai a paleta de cores

    # 3. Processar o círculo e a paleta
    target_color = get_target_color(circle)  # Codigo extrai a cor alvo do circulo
    camera_colors = get_camera_colors(palette)  # Codigo que extrai as cores da paleta

    # 4. Aplicar a correção de cores
    corrected_color = correct_color(camera_colors, target_color) #Retorna a cor corrida

    # 5. Retornar a cor corrigida para o front-end
    print("Cor corrigida:", corrected_color)
    return corrected_color.tolist()  # Converte para lista para facilitar o uso no front-end

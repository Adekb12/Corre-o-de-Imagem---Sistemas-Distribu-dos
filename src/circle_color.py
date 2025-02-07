from PIL import Image
import numpy as np

def get_circle_color(image):
    """
    Extrai a cor média de pontos próximos ao centro de um círculo em uma imagem.

    Parâmetros:
        image_path (str): Caminho da imagem contendo o círculo.
        num_points (int): Número de pontos próximos ao centro a serem amostrados.

    Retorna:
        np.array: Cor média no formato RGB (1 x 3).
    """
    
    try:
        image = image.convert("RGB")
        width, height = image.size
        image_array = np.array(image)

        center_x, center_y = width // 2, height // 2
        radius = 10  
        num_points = 5  

        angles = np.linspace(0, 2 * np.pi, num_points)
        x_coords = (center_x + radius * np.cos(angles)).astype(int)
        y_coords = (center_y + radius * np.sin(angles)).astype(int)

        colors = [image_array[y, x] for x, y in zip(x_coords, y_coords) if 0 <= x < width and 0 <= y < height]
        print(np.mean(colors, axis=0).astype(int))
        if colors:
            return np.mean(colors, axis=0).astype(int)
        else:
            raise ValueError("Nenhum ponto válido foi encontrado no círculo.")

    except Exception as e:
        print(f"Erro ao extrair a cor alvo: {e}")
        return None

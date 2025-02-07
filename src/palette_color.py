import numpy as np

def get_palette_color(image, grid_rows=4, grid_cols=6, margin=5):
    try:
        if not isinstance(image, np.ndarray):
            image = np.array(image) 
        
        height, width, _ = image.shape
        block_height = height // grid_rows
        block_width = width // grid_cols
        colors = []

        for row in range(grid_rows):
            for col in range(grid_cols):
                start_x = col * block_width + margin
                start_y = row * block_height + margin
                end_x = (col + 1) * block_width - margin
                end_y = (row + 1) * block_height - margin
                block = image[start_y:end_y, start_x:end_x]
                mask = np.all(block > [10, 10, 10], axis=-1)
                if np.any(mask):
                    average_color = block[mask].mean(axis=0)
                    colors.append(average_color)
                else:
                    colors.append([0, 0, 0])
            
        return np.array(colors)

    except Exception as e:
        print(f"Erro ao extrair cores da paleta: {e}")
        return None

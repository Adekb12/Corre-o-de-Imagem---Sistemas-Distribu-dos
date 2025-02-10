import numpy as np
from sklearn.linear_model import LinearRegression

# Dados RGB originais fixos
rgb_original = np.array([
    [117, 80, 65],
    [199, 144, 128],
    [80, 120, 155],
    [97, 108, 64],
    [124, 128, 174],
    [97, 189, 173],
    [230, 124, 48],
    [42, 91, 168],
    [200, 81, 94],
    [89, 58, 102],
    [166, 187, 63],
    [234, 161, 42],
    [3, 65, 146],
    [71, 147, 71],
    [186, 55, 62],
    [249, 200, 41],
    [183, 78, 140],
    [1, 132, 164],
    [242, 241, 235],
    [202, 202, 200],
    [161, 163, 163],
    [120, 120, 119],
    [83, 84, 84],
    [49, 49, 50]
])

def color_correction(rgb_camera, rgb_target):
    """
    Corrige a cor de um pixel com base nas cores da câmera e nas cores originais.

    Parâmetros:
        rgb_camera (np.array): Array de cores capturadas pela câmera (N x 3).
        rgb_target (np.array): Cor específica a ser corrigida (1 x 3).

    Retorna:
        np.array: Cor corrigida (1 x 3).
    """

    model_r = LinearRegression()
    model_g = LinearRegression()
    model_b = LinearRegression()

    model_r.fit(rgb_camera, rgb_original[:, 0])
    model_g.fit(rgb_camera, rgb_original[:, 1])
    model_b.fit(rgb_camera, rgb_original[:, 2])

    def apply_correction(rgb):
        r = model_r.predict(rgb)
        g = model_g.predict(rgb)
        b = model_b.predict(rgb)
        return np.column_stack((r, g, b))

    corrected_rgb_target = apply_correction(rgb_target.reshape(1, -1))
    corrected_rgb_target = np.clip(corrected_rgb_target, 0, 255).astype(int)

    return corrected_rgb_target[0]

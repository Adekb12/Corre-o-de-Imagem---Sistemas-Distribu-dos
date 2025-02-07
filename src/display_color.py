import numpy as np
import matplotlib.pyplot as plt

def display_color(color):
    color_image = np.ones((100, 100, 3), dtype=np.uint8) * color
    plt.imshow(color_image)
    plt.axis('off')
    plt.show()
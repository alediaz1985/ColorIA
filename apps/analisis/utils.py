# apps/analisis/utils.py

from PIL import Image
import numpy as np
from collections import Counter

def detectar_color(path_imagen):
    # Convertir a RGB para asegurar que tenga 3 canales
    imagen = Image.open(path_imagen).convert("RGB").resize((100, 100))
    
    # Convertir a array de píxeles
    pixels = np.array(imagen).reshape(-1, 3)

    # Colores básicos definidos
    colores = {
        "rojo": (255, 0, 0),
        "verde": (0, 255, 0),
        "azul": (0, 0, 255),
        "amarillo": (255, 255, 0),
        "negro": (0, 0, 0),
        "blanco": (255, 255, 255),
        "gris": (128, 128, 128)
    }

    def color_cercano(pixel):
        distancias = {
            nombre: np.linalg.norm(np.array(pixel) - np.array(rgb))
            for nombre, rgb in colores.items()
        }
        return min(distancias, key=distancias.get)

    # Calcular el color predominante
    colores_detectados = [color_cercano(p) for p in pixels]
    color_predominante = Counter(colores_detectados).most_common(1)[0][0]
    return color_predominante

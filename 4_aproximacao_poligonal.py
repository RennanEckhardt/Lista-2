"""
4_aproximacao_poligonal.py
--------------------------
Representação geométrica da bola através da Aproximação Poligonal (Douglas-Peucker).
Desenha o polígono sobre o contorno detectado da bola.

Autor: Rennan Moreira
Disciplina: Processamento e Análise de Imagens
Data: Novembro/2025
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Carrega novamente a imagem, se necessário
img = cv.imread('bola.jpg', cv.IMREAD_GRAYSCALE)

if img is None:
    print("Erro: não foi possível carregar a imagem 'bola.jpg'.")
else:
    # --- Limiarização para gerar contornos ---
    _, binary_mask = cv.threshold(img, 150, 255, cv.THRESH_BINARY_INV)

    contours, _ = cv.findContours(binary_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv.contourArea)

        # --- Aproximação Poligonal ---
        epsilon = 0.01 * cv.arcLength(largest_contour, True)
        approximated_polygon = cv.approxPolyDP(largest_contour, epsilon, True)

        # --- Converte para RGB para desenhar em cor ---
        img_to_display = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
        cv.drawContours(img_to_display, [approximated_polygon], -1, (255, 0, 0), 2)

        # --- Exibição ---
        plt.figure(figsize=(8, 8))
        plt.imshow(cv.cvtColor(img_to_display, cv.COLOR_BGR2RGB))
        plt.title('Resultado da Aproximação Poligonal')
        plt.xticks([]), plt.yticks([])
        plt.show()
    else:
        print("Nenhum contorno encontrado para aplicar a aproximação poligonal.")

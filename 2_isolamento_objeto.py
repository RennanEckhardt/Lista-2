"""
2_isolamento_objeto.py
----------------------
Segmentação e isolamento do objeto principal (bola) a partir da imagem 'bola.jpg'.
O script aplica limiarização, operações morfológicas e detecção de contornos.

Autor: Rennan Moreira
Disciplina: Processamento e Análise de Imagens
Data: Novembro/2025
"""

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# Leitura da imagem em escala de cinza
img = cv.imread('bola.jpg', cv.IMREAD_GRAYSCALE)

if img is None:
    print("Erro: não foi possível carregar a imagem 'bola.jpg'.")
else:
    # --- Limiarização binária inversa ---
    _, binary_mask = cv.threshold(img, 150, 255, cv.THRESH_BINARY_INV)

    # --- Operações morfológicas para limpeza de ruídos ---
    kernel = np.ones((5, 5), np.uint8)
    binary_mask = cv.morphologyEx(binary_mask, cv.MORPH_OPEN, kernel)
    binary_mask = cv.morphologyEx(binary_mask, cv.MORPH_CLOSE, kernel)

    # --- Detecção de contornos ---
    contours, _ = cv.findContours(binary_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv.contourArea)

        # --- Criação da imagem com o objeto isolado ---
        isolated_object_img = np.zeros_like(img)
        cv.drawContours(isolated_object_img, [largest_contour], -1, 255, -1)

        # --- Exibição dos resultados ---
        plt.figure(figsize=(10, 5))
        plt.subplot(121), plt.imshow(binary_mask, cmap='gray')
        plt.title('Máscara Binária'), plt.xticks([]), plt.yticks([])

        plt.subplot(122), plt.imshow(isolated_object_img, cmap='gray')
        plt.title('Objeto Isolado'), plt.xticks([]), plt.yticks([])

        plt.show()

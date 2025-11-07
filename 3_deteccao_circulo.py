"""
3_deteccao_circulo.py
---------------------
Detecção da bola na imagem por meio da Transformada de Hough.
Identifica automaticamente círculos e gera uma máscara com a bola isolada.

Autor: Rennan Moreira
Disciplina: Processamento e Análise de Imagens
Data: Novembro/2025
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Leitura da imagem
img = cv.imread('bola.jpg', cv.IMREAD_GRAYSCALE)

if img is None:
    print("Erro: não foi possível carregar a imagem 'bola.jpg'.")
else:
    # --- Suavização da imagem ---
    img_blur = cv.medianBlur(img, 5)

    # --- Detecção de círculos (Transformada de Hough) ---
    circles = cv.HoughCircles(
        img_blur,
        cv.HOUGH_GRADIENT,
        dp=1,
        minDist=50,
        param1=100,
        param2=30,
        minRadius=0,
        maxRadius=0
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))

        # --- Seleciona o primeiro círculo detectado ---
        ball_circle = circles[0, 0]
        center = (ball_circle[0], ball_circle[1])
        radius = ball_circle[2]

        # --- Cria máscara circular ---
        mask = np.zeros_like(img, dtype=np.uint8)
        cv.circle(mask, center, radius, 255, -1)

        # --- Isola a bola ---
        isolated_ball = cv.bitwise_and(img, img, mask=mask)

        # --- Exibe resultados ---
        plt.figure(figsize=(10, 5))
        plt.subplot(121), plt.imshow(isolated_ball, cmap='gray')
        plt.title('Bola Isolada'), plt.xticks([]), plt.yticks([])

        plt.subplot(122), plt.imshow(mask, cmap='gray')
        plt.title('Máscara da Bola'), plt.xticks([]), plt.yticks([])

        plt.show()
    else:
        print("Nenhum círculo foi detectado.")

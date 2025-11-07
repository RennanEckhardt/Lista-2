"""
1_canny_sobel.py
----------------
Aplicação dos algoritmos de detecção de bordas Canny e Sobel.
Este script compara visualmente os dois métodos aplicados à imagem 'bola.jpg'.

Autor: Rennan Moreira
Disciplina: Processamento e Análise de Imagens
Data: Novembro/2025
"""

import cv2 as cv
from matplotlib import pyplot as plt

# Caminho da imagem
img_path = 'bola.jpg'
print(f"Processing image: {img_path}")

# Leitura da imagem em escala de cinza
img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

# Verifica se a imagem foi carregada corretamente
if img is None:
    print(f"Erro: não foi possível carregar a imagem {img_path}.")
else:
    # --- Método Canny ---
    edges_canny = cv.Canny(img, 100, 200)

    # --- Método Sobel ---
    scale = 1
    delta = 0
    ddepth = cv.CV_16S

    grad_x = cv.Sobel(img, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(img, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)

    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    edges_sobel = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    # --- Exibição dos resultados ---
    plt.figure(figsize=(15, 5))
    plt.subplot(131), plt.imshow(img, cmap='gray')
    plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(132), plt.imshow(edges_canny, cmap='gray')
    plt.title('Bordas - Canny'), plt.xticks([]), plt.yticks([])

    plt.subplot(133), plt.imshow(edges_sobel, cmap='gray')
    plt.title('Bordas - Sobel'), plt.xticks([]), plt.yticks([])

    plt.show()

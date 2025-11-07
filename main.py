"""
main.py
-------
Execução completa do projeto de segmentação e representação geométrica de uma bola.
Este script integra todas as etapas:
1. Detecção de bordas (Canny e Sobel)
2. Isolamento do objeto principal
3. Detecção de círculos (Transformada de Hough)
4. Aproximação poligonal (Douglas-Peucker)

Autor: Rennan Moreira
Disciplina: Processamento e Análise de Imagens
Data: Novembro/2025
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# ==============================
#  Funções auxiliares
# ==============================

def detectar_bordas(img):
    """Aplica os algoritmos de Canny e Sobel na imagem."""
    edges_canny = cv.Canny(img, 100, 200)

    grad_x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=3)
    grad_y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=3)

    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    edges_sobel = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    return edges_canny, edges_sobel


def isolar_objeto(img):
    """Segmenta e isola o objeto principal através de limiarização e morfologia."""
    _, binary_mask = cv.threshold(img, 150, 255, cv.THRESH_BINARY_INV)
    kernel = np.ones((5, 5), np.uint8)
    binary_mask = cv.morphologyEx(binary_mask, cv.MORPH_OPEN, kernel)
    binary_mask = cv.morphologyEx(binary_mask, cv.MORPH_CLOSE, kernel)

    contours, _ = cv.findContours(binary_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    isolated = np.zeros_like(img)
    if contours:
        largest = max(contours, key=cv.contourArea)
        cv.drawContours(isolated, [largest], -1, 255, -1)

    return binary_mask, isolated


def detectar_circulo(img):
    """Detecta o círculo da bola usando a Transformada de Hough."""
    blur = cv.medianBlur(img, 5)
    circles = cv.HoughCircles(
        blur, cv.HOUGH_GRADIENT, dp=1, minDist=50,
        param1=100, param2=30, minRadius=0, maxRadius=0
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        c = circles[0, 0]
        mask = np.zeros_like(img, dtype=np.uint8)
        cv.circle(mask, (c[0], c[1]), c[2], 255, -1)
        isolated = cv.bitwise_and(img, img, mask=mask)
        return isolated, mask, (c[0], c[1]), c[2]
    else:
        return None, None, None, None


def aproximacao_poligonal(img):
    """Realiza a aproximação poligonal do contorno da bola."""
    _, binary_mask = cv.threshold(img, 150, 255, cv.THRESH_BINARY_INV)
    contours, _ = cv.findContours(binary_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv.contourArea)
        epsilon = 0.01 * cv.arcLength(largest, True)
        approx = cv.approxPolyDP(largest, epsilon, True)
        color_img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
        cv.drawContours(color_img, [approx], -1, (255, 0, 0), 2)
        return color_img
    else:
        return None


# ==============================
#  Execução principal
# ==============================

def main():
    img = cv.imread('bola.jpg', cv.IMREAD_GRAYSCALE)
    if img is None:
        print("Erro: não foi possível carregar a imagem 'bola.jpg'.")
        return

    # 1️⃣ Detecção de Bordas
    edges_canny, edges_sobel = detectar_bordas(img)
    plt.figure(figsize=(15, 5))
    plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Original')
    plt.subplot(132), plt.imshow(edges_canny, cmap='gray'), plt.title('Canny')
    plt.subplot(133), plt.imshow(edges_sobel, cmap='gray'), plt.title('Sobel')
    plt.suptitle('1️⃣ Detecção de Bordas')
    plt.show()

    # 2️⃣ Isolamento do Objeto
    binary_mask, isolated = isolar_objeto(img)
    plt.figure(figsize=(10, 5))
    plt.subplot(121), plt.imshow(binary_mask, cmap='gray'), plt.title('Máscara Binária')
    plt.subplot(122), plt.imshow(isolated, cmap='gray'), plt.title('Objeto Isolado')
    plt.suptitle('2️⃣ Isolamento do Objeto')
    plt.show()

    # 3️⃣ Detecção de Círculo
    isolated_ball, mask, center, radius = detectar_circulo(img)
    if isolated_ball is not None:
        plt.figure(figsize=(10, 5))
        plt.subplot(121), plt.imshow(isolated_ball, cmap='gray'), plt.title('Bola Isolada')
        plt.subplot(122), plt.imshow(mask, cmap='gray'), plt.title('Máscara do Círculo')
        plt.suptitle('3️⃣ Detecção de Círculo (Hough)')
        plt.show()
    else:
        print("Nenhum círculo detectado na imagem.")

    # 4️⃣ Aproximação Poligonal
    poly_img = aproximacao_poligonal(img)
    if poly_img is not None:
        plt.figure(figsize=(8, 8))
        plt.imshow(cv.cvtColor(poly_img, cv.COLOR_BGR2RGB))
        plt.title('4️⃣ Aproximação Poligonal da Bola')
        plt.show()
    else:
        print("Não foi possível realizar a aproximação poligonal.")


if __name__ == "__main__":
    main()

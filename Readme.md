🧾 README.md
# 🧠 Segmentação e Representação Geométrica de Regiões

Este projeto faz parte de um trabalho prático da disciplina **Processamento e Análise de Imagens**, com o objetivo de comparar diferentes métodos de segmentação e representar geometricamente objetos detectados em uma imagem real.

As implementações foram feitas em **Python**, utilizando as bibliotecas **OpenCV**, **NumPy** e **Matplotlib**.

---

## 📁 Estrutura do Projeto



📦 Segmentacao-Geometria
┣ 📜 1_canny_sobel.py
┣ 📜 2_isolamento_objeto.py
┣ 📜 3_deteccao_circulo.py
┣ 📜 4_aproximacao_poligonal.py
┗ 📜 README.md


---

## ⚙️ Requisitos

Certifique-se de ter as bibliotecas abaixo instaladas:

```bash
pip install opencv-python matplotlib numpy

🧩 Etapas do Projeto
🧱 1. Detecção de Bordas (Canny e Sobel)

Arquivo: 1_canny_sobel.py

Neste script, são aplicados dois métodos clássicos de detecção de bordas:

Canny: utiliza suavização gaussiana, cálculo de gradiente e limiarização por histerese.

Sobel: calcula o gradiente da intensidade nos eixos X e Y.

Ambos os resultados são comparados lado a lado com a imagem original.

python 1_canny_sobel.py


Saída esperada:

Imagem original

Bordas com Canny

Bordas com Sobel

Essas bordas são fundamentais para isolar regiões e contornos em etapas posteriores.

⚪ 2. Isolamento do Objeto de Interesse

Arquivo: 2_isolamento_objeto.py

Aqui ocorre a segmentação da bola presente na imagem bola.jpg.
O código aplica:

Limiarização binária (threshold)

Operações morfológicas (abertura e fechamento)

Detecção do maior contorno — considerado o objeto principal.

O resultado é uma máscara binária e uma imagem com o objeto isolado.

python 2_isolamento_objeto.py


Saída esperada:

Máscara binária

Objeto isolado

⚙️ 3. Detecção de Círculo (Transformada de Hough)

Arquivo: 3_deteccao_circulo.py

Este script identifica a forma circular do objeto (bola) por meio da Transformada de Hough.

Etapas:

Suavização da imagem com medianBlur();

Aplicação de cv.HoughCircles() para detectar círculos;

Criação de uma máscara circular correspondente à bola;

Isolamento da bola usando operação bitwise.

python 3_deteccao_circulo.py


Saída esperada:

Bola isolada

Máscara circular

🔺 4. Representação Geométrica (Aproximação Poligonal)

Arquivo: 4_aproximacao_poligonal.py

Esta etapa realiza a representação geométrica do contorno da bola utilizando a técnica de Aproximação Poligonal (algoritmo de Douglas-Peucker).
O objetivo é reduzir a complexidade do contorno, mantendo a forma principal do objeto.

A função cv.drawContours() desenha o polígono sobre a imagem original ou sobre a bola isolada.

python 4_aproximacao_poligonal.py


Saída esperada:

Contorno da bola com o polígono aproximado sobreposto

🧠 Funcionamento Geral

O pipeline completo pode ser entendido da seguinte forma:

Entrada: imagem bola.jpg

Pré-processamento: conversão em tons de cinza

Segmentação: uso de Canny ou Sobel

Isolamento: extração do maior contorno

Detecção de forma: reconhecimento circular com Hough

Descrição geométrica: simplificação por aproximação poligonal

📸 Resultados Esperados
Etapa	Resultado
Detecção de bordas	Bordas precisas (Canny) e gradientes (Sobel)
Isolamento	Objeto separado da cena
Hough	Máscara circular representando a bola
Aproximação Poligonal	Forma simplificada do contorno
💡 Conclusão

O projeto demonstra a integração entre métodos de segmentação, filtragem e representação geométrica, evidenciando como diferentes técnicas podem ser combinadas para descrever e analisar objetos em imagens.

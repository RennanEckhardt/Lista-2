# 🎯 Segmentação e Representação Geométrica de Imagens

> **Disciplina:** Processamento e Análise de Imagens  
> **Instituição:** Pontifícia Universidade Católica de Minas Gerais  
> **Autor:** Rennan Moreira  
> **Data:** Novembro de 2025

---

## 📋 Sobre o Projeto

Este projeto implementa um pipeline completo de **processamento digital de imagens** para segmentação, detecção e representação geométrica de objetos. O trabalho foca na análise de uma bola, aplicando técnicas clássicas de visão computacional para:

- Detectar bordas e contornos
- Isolar objetos do fundo
- Identificar formas geométricas (círculos)
- Simplificar representações complexas

O projeto está dividido em módulos independentes que podem ser executados separadamente ou através de um script unificado.

---

## 🧩 Estrutura do Pipeline

### **1. Detecção de Bordas** → `1_canny_sobel.py`

Aplica dois algoritmos clássicos de detecção de bordas para realçar contornos na imagem:

- **Canny**: Detector multiestágio com supressão não-máxima e histerese
  - Gera bordas finas, contínuas e precisas
  - Robusto a ruídos graças à suavização Gaussiana
  - Sensível à escolha dos limiares (100 e 200)

- **Sobel**: Operador baseado em gradientes direcionais
  - Simples e computacionalmente eficiente
  - Produz bordas mais espessas e menos definidas
  - Mais sensível a variações locais de intensidade

**Saída:** Comparação visual entre bordas detectadas por Canny e Sobel

---

### **2. Isolamento do Objeto** → `2_isolamento_objeto.py`

Segmenta o objeto principal (bola) utilizando técnicas de processamento morfológico:

**Técnicas aplicadas:**
- **Limiarização binária** (`cv.threshold`) — Separa objeto do fundo
- **Operações morfológicas** (`cv.morphologyEx`) — Remove ruídos com abertura/fechamento
- **Detecção de contornos** (`cv.findContours`) — Identifica regiões conectadas
- **Seleção por área** — Isola o maior contorno (objeto de interesse)

**Saída:** Máscara binária e objeto isolado com fundo removido

---

### **3. Detecção de Círculos** → `3_deteccao_circulo.py`

Utiliza a **Transformada de Hough** para reconhecer formas circulares:

**Processo:**
1. Suavização da imagem para reduzir falsos positivos
2. Aplicação de `cv.HoughCircles` com parâmetros otimizados
3. Criação de máscara circular precisa
4. Isolamento do interior do círculo detectado

**Saída:** Bola segmentada com precisão circular e máscara correspondente

---

### **4. Aproximação Poligonal** → `4_aproximacao_poligonal.py`

Simplifica o contorno do objeto usando o **algoritmo de Douglas-Peucker**:

**Características:**
- Reduz a complexidade do contorno preservando sua forma geral
- Parâmetro ε = 0.01 × perímetro controla a precisão
- Redução de 1760 vértices → 21 vértices no exemplo
- Útil para representação geométrica e análise de formas

**Saída:** Contorno poligonal simplificado sobre a imagem isolada

---

## 🚀 Execução

### **Executar o pipeline completo:**
```bash
python main.py
```

### **Executar módulos individualmente:**
```bash
python 1_canny_sobel.py
python 2_isolamento_objeto.py
python 3_deteccao_circulo.py
python 4_aproximacao_poligonal.py
```

---

## 📦 Dependências

```bash
pip install opencv-python numpy matplotlib
```

**Requisitos:**
- Python 3.7+
- OpenCV 4.x
- NumPy
- Matplotlib

---

## 📊 Resultados

O projeto demonstra a eficácia de diferentes técnicas de processamento:

| Técnica | Vantagens | Limitações |
|---------|-----------|------------|
| **Canny** | Bordas finas e precisas, robusto a ruído | Sensível aos parâmetros |
| **Sobel** | Rápido e simples | Bordas espessas, sensível a ruído |
| **Hough** | Detecção precisa de formas circulares | Requer ajuste de parâmetros |
| **Douglas-Peucker** | Simplificação eficiente | Pode perder detalhes importantes |

---

## 🧠 Conceitos Abordados

- **Detecção de bordas**: Identificação de descontinuidades de intensidade
- **Limiarização**: Segmentação por níveis de intensidade
- **Morfologia matemática**: Operações de abertura, fechamento e erosão
- **Transformada de Hough**: Reconhecimento de formas geométricas
- **Aproximação poligonal**: Simplificação de contornos complexos

---

## 📁 Estrutura do Repositório

```
.
├── 1_canny_sobel.py              # Detecção de bordas
├── 2_isolamento_objeto.py         # Segmentação do objeto
├── 3_deteccao_circulo.py          # Detecção via Hough
├── 4_aproximacao_poligonal.py     # Simplificação de contorno
├── main.py                        # Pipeline completo
├── README.md                      # Documentação
└── imagens/                       # Recursos de entrada
```

---

## 🔗 Links Úteis

- **Google Colab**: [Projeto Online](https://colab.research.google.com/drive/1V1q9SLXy8c1I6JLVcnQj9QC0_P4Ul6Sx?usp=sharing)
- **Repositório GitHub**: [Lista-2](https://github.com/RennanEckhardt/Lista-2/tree/main)

---

## 📖 Relatório Técnico

Para uma análise detalhada dos algoritmos, resultados experimentais e discussão teórica, consulte o relatório completo em formato LaTeX incluído no repositório.

**Destaques do relatório:**
- Fundamentação teórica dos algoritmos Canny e Sobel
- Comparação qualitativa entre métodos de detecção
- Análise de técnicas de representação geométrica
- Discussão sobre aplicações e contextos de uso

---

## 📝 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte da disciplina de Processamento e Análise de Imagens.

---

**Desenvolvido com 💙 por Rennan Moreira**

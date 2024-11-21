# Correção de Cores para Imagens de Café

- Disciplina: Sistemas Distribuídos
- Integrantes: Bruno Henrique Firmino, Gabriel Furtado Teixeira, Lucas de Castro Nízio, Rhuan Campidelli Borges

## Objetivo
O projeto visa identificar e corrigir as cores dos cafés em imagens, usando uma paleta de cores padrão para calibração. A técnica aplicada permite uma correção precisa dos valores RGB nas imagens do café torrado, tornando-as mais consistentes e aproximadas da realidade, independentemente das condições de captura da foto.

## Funcionalidades
- Detecção de Paleta: Utiliza técnicas de visão computacional para detectar uma paleta de cores fixa em uma imagem.
- Correção de RGB: Ajusta os valores RGB da amostra de café para alinhar com as cores da paleta detectada.
- Detectar Ponto de Torra: Com o RGB do café encontrado, detectar qual é o ponto de torra do café de acordo com valores já conhecidos.

## Tecnologias Utilizadas
- Python: Linguagem principal para processamento de imagens.
- YOLO (futuro): Planejamento para detecção automatizada da paleta de cores usando modelos de aprendizado de máquina.

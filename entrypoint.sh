#!/bin/sh
echo "Iniciando Ollama..."

# Inicia o Ollama em background
ollama serve &

# Aguarda um curto período para garantir que o serviço está rodando
sleep 5

# Baixa o modelo llama3
echo "Baixando modelo llama3..."
ollama pull llama3

# Mantém o container rodando
wait

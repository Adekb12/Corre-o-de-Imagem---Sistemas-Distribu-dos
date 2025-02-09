FROM ollama/ollama:latest

# Copia o script para dentro do container
COPY entrypoint.sh /entrypoint.sh

# Define o script como ponto de entrada
ENTRYPOINT ["sh", "/entrypoint.sh"]

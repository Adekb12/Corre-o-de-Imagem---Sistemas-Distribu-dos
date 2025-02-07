# Projeto de Correção de Cores em Imagens

Este projeto tem como objetivo corrigir as cores de uma imagem com base em uma paleta de cores de referência. Ele é composto por um servidor Flask que recebe uma imagem, detecta um círculo (ou região de interesse), extrai uma paleta de cores da imagem e aplica uma correção de cores usando regressão linear. A cor corrigida é então retornada como resposta.

## Funcionalidades

- **Recebimento de Imagem**: O servidor recebe uma imagem via requisição HTTP.
- **Detecção de Círculo**: Detecta um círculo na imagem e extrai a cor alvo.
- **Extração de Paleta**: Detecta uma paleta de cores na imagem e extrai as cores da paleta.
- **Correção de Cores**: Usa regressão linear para corrigir a cor alvo com base na paleta de cores.
- **Resposta JSON**: Retorna a cor corrigida em formato JSON.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python: flask, pillow, numpy, scikit-learn

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

1. Inicie o servidor Flask:
    ```bash
    python main.py
    ```

    O servidor estará disponível em http://localhost:5000.

2. Envie uma imagem para o servidor usando curl ou qualquer cliente HTTP:
    ```bash
    curl -X POST -F "image=@caminho/para/sua/imagem.jpg" http://localhost:5000/process_image
    ```

    A resposta será um JSON com a cor corrigida:
    ```json
    {
      "corrected_color": [123, 145, 167]
    }
    ```

## Estrutura do Projeto

```bash
meu_servidor/
│
├── color_correction.py  # Código de correção de cores
├── main.py              # Servidor Flask
├── README.md            # Documentação do projeto
└── requirements.txt     # Dependências do projeto
```

## Contribuidores

- **Bruno Henrique Firmino** - [GitHub](https://github.com/Bruno7k) 
- **Gabriel Furtado Teixeira** - [GitHub](https://github.com/GabrielFTgft) 
- **Lucas de Castros Nízio** - [GitHub](https://github.com/lucasnizio)
- **Rhuan Campideli** - [GitHub](https://github.com/rhuancborges)

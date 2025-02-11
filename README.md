# Projeto de Correção de Cores em Imagens

Este projeto tem como objetivo corrigir as cores de uma imagem com base em uma paleta de cores de referência. Ele é composto por um servidor Flask que recebe uma imagem, detecta um círculo (ou região de interesse), extrai uma paleta de cores da imagem e aplica uma correção de cores usando regressão linear. A cor corrigida é então retornada como resposta.

## Funcionalidades

- **Recebimento de Imagem**: O servidor recebe uma imagem via requisição HTTP.
- **Detecção de Círculo**: Detecta um círculo na imagem e extrai a cor alvo.
- **Extração de Paleta**: Detecta uma paleta de cores na imagem e extrai as cores da paleta.
- **Correção de Cores**: Usa regressão linear para corrigir a cor alvo com base na paleta de cores.
- **Resposta do Ollama**: Retorna uma resposta melhorada da cor corrigida.

## Contribuidores

- **Bruno Henrique Firmino** - [GitHub](https://github.com/Bruno7k) 
- **Gabriel Furtado Teixeira** - [GitHub](https://github.com/GabrielFTgft) 
- **Lucas de Castros Nízio** - [GitHub](https://github.com/lucasnizio)
- **Rhuan Campideli** - [GitHub](https://github.com/rhuancborges)

# Engenharia de Dados com Arquitetura Medalhão

Este repositório apresenta uma estrutura simples de pastas para projetos de engenharia de dados utilizando Python seguindo o padrão Medalhão (Bronze, Silver e Gold). Use como ponto de partida para organizar scripts de ingestão e processamento.

## Estrutura sugerida

- `data/bronze` – armazena dados brutos recebidos na ingestão.
- `data/silver` – contém dados tratados e normalizados.
- `data/gold` – guarda dados prontos para consumo analítico.
- `src/ingestion` – scripts Python responsáveis por ingestão e carga inicial.
- `src/transformation` – scripts de transformação e limpeza dos dados.
- `notebooks` – exploração e documentação de uso interativo.
- `tests` – testes automatizados do projeto.

Adapte esta estrutura às necessidades do seu projeto.

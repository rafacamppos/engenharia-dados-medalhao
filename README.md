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

## Exportar Parquet para Cosmos DB

Utilize o script `src/adapters/cosmos/upload_parquet.py` para ler um arquivo Parquet e inserir os registros em um container do Azure Cosmos DB. Configure as seguintes variáveis de ambiente antes de executar:

- `PARQUET_PATH` – caminho do arquivo parquet de origem
- `COSMOS_ENDPOINT` – URL do endpoint do Cosmos DB
- `COSMOS_KEY` – chave de acesso do Cosmos DB
- `COSMOS_DATABASE` – nome do banco de dados
- `COSMOS_CONTAINER` – nome do container

Exemplo de execução:

```bash
python src/adapters/cosmos/upload_parquet.py
```

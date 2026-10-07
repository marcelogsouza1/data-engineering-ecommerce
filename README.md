# E-commerce Data Engineering Pipeline

Pipeline de Engenharia de Dados desenvolvido em **Python** para simular o processamento de dados de um e-commerce, contemplando ingestão, validação, transformação e disponibilização de dados para análises de negócio.

O projeto foi construído com foco em boas práticas de organização de pipelines, qualidade de dados e separação entre dados brutos, processados e analíticos.

---

## Visão Geral

O pipeline recebe dados de **clientes, produtos e pedidos** em formato CSV, realiza validações de qualidade, integra as diferentes fontes, calcula métricas de faturamento e disponibiliza datasets preparados para análises.

### Fluxo de processamento

```text
                    ┌────────────────────┐
                    │    Dados Raw       │
                    │       CSV          │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │     Ingestion      │
                    │      Python        │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      Data          │
                    │     Validation     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │  Transformation   │
                    │      Pandas        │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   Processed Data   │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      Analytics     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Analytics Datasets │
                    └────────────────────┘
```

---

## Objetivos

O projeto tem como principais objetivos:

* Implementar um pipeline de processamento de dados utilizando Python.
* Separar dados em diferentes camadas de processamento.
* Aplicar regras de qualidade e validação.
* Integrar múltiplas fontes de dados.
* Realizar transformações utilizando Pandas.
* Criar métricas de negócio a partir dos dados processados.
* Disponibilizar datasets estruturados para consumo analítico.
* Aplicar conceitos utilizados em projetos de Engenharia de Dados.

---

## Arquitetura de Dados

O projeto utiliza uma organização em camadas:

### Raw

Contém os dados originalmente ingeridos, sem transformações.

```text
data/raw/
├── clientes.csv
├── produtos.csv
└── pedidos.csv
```

### Processed

Contém os dados a

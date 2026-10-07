import pandas as pd

arquivo = "data/processed/pedidos_processados.csv"

dados = pd.read_csv(arquivo)

# Faturamento por cliente
faturamento_cliente = (
    dados.groupby(["cliente_id", "nome"])["faturamento"]
    .sum()
    .reset_index()
    .sort_values("faturamento", ascending=False)
)

faturamento_cliente.to_csv(
    "data/analytics/faturamento_por_cliente.csv",
    index=False,
    encoding="utf-8"
)

# Faturamento por produto
faturamento_produto = (
    dados.groupby(["produto_id", "produto"])["faturamento"]
    .sum()
    .reset_index()
    .sort_values("faturamento", ascending=False)
)

faturamento_produto.to_csv(
    "data/analytics/faturamento_por_produto.csv",
    index=False,
    encoding="utf-8"
)

# Faturamento por categoria
faturamento_categoria = (
    dados.groupby("categoria")["faturamento"]
    .sum()
    .reset_index()
    .sort_values("faturamento", ascending=False)
)

faturamento_categoria.to_csv(
    "data/analytics/faturamento_por_categoria.csv",
    index=False,
    encoding="utf-8"
)

print("Arquivos de analytics gerados com sucesso!")

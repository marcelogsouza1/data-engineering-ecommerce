import pandas as pd

arquivo = "data/processed/pedidos_processados.csv"

dados = pd.read_csv(arquivo)

print("=== ANÁLISE DE VENDAS ===")

# Faturamento por cliente
faturamento_cliente = (
    dados.groupby("nome")["faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\nFaturamento por cliente:")
print(faturamento_cliente)

# Faturamento por produto
faturamento_produto = (
    dados.groupby("produto")["faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\nFaturamento por produto:")
print(faturamento_produto)

# Faturamento por categoria
faturamento_categoria = (
    dados.groupby("categoria")["faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\nFaturamento por categoria:")
print(faturamento_categoria)

# Quantidade vendida por produto
quantidade_produto = (
    dados.groupby("produto")["quantidade"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQuantidade vendida por produto:")
print(quantidade_produto)

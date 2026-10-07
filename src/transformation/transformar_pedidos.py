import pandas as pd

# Arquivos de entrada
clientes = pd.read_csv("data/raw/clientes.csv")
produtos = pd.read_csv("data/raw/produtos.csv")
pedidos = pd.read_csv("data/raw/pedidos.csv")

# Converter data
pedidos["data_pedido"] = pd.to_datetime(pedidos["data_pedido"])

# JOIN entre pedidos e clientes
pedidos_clientes = pedidos.merge(
    clientes,
    on="cliente_id",
    how="left"
)

# JOIN entre pedidos e produtos
dados_completos = pedidos_clientes.merge(
    produtos,
    on="produto_id",
    how="left"
)

# Calcular faturamento
dados_completos["faturamento"] = (
    dados_completos["quantidade"] * dados_completos["preco"]
)

# Salvar dados processados
dados_completos.to_csv(
    "data/processed/pedidos_processados.csv",
    index=False,
    encoding="utf-8"
)

print("=== DADOS PROCESSADOS ===")
print(dados_completos)

print("\nArquivo salvo com sucesso!")
print("Total de registros:", len(dados_completos))
print("Faturamento total: R$", dados_completos["faturamento"].sum())

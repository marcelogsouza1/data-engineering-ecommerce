import pandas as pd

arquivo = "data/raw/clientes.csv"

clientes = pd.read_csv(arquivo)

print("Dados carregados do CSV:")
print(clientes)

print("\nQuantidade de registros:")
print(len(clientes))

print("\nColunas:")
print(clientes.columns.tolist())

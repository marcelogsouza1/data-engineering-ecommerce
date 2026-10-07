import pandas as pd

dados_clientes = {
    "cliente_id": [1, 2, 3, 4, 5],
    "nome": ["João", "Maria", "Carlos", "Ana", "Pedro"],
    "idade": [25, 32, 41, 28, 35],
    "estado": ["SP", "RJ", "MG", "SP", "PR"]
}

clientes = pd.DataFrame(dados_clientes)

print("Dados dos clientes:")
print(clientes)

print("\nInformações do DataFrame:")
print(clientes.info())

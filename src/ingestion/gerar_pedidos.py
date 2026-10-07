import pandas as pd

dados_pedidos = {
    "pedido_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "cliente_id": [1, 2, 3, 1, 4, 5, 2, 3],
    "produto_id": [101, 102, 103, 104, 105, 101, 104, 102],
    "quantidade": [1, 2, 1, 1, 2, 1, 1, 3],
    "data_pedido": [
        "2026-10-01",
        "2026-10-01",
        "2026-10-02",
        "2026-10-03",
        "2026-10-03",
        "2026-10-04",
        "2026-10-05",
        "2026-10-05"
    ]
}

pedidos = pd.DataFrame(dados_pedidos)

pedidos.to_csv(
    "data/raw/pedidos.csv",
    index=False,
    encoding="utf-8"
)

print("Arquivo pedidos.csv criado com sucesso!")
print(pedidos)

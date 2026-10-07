import pandas as pd

dados_produtos = {
    "produto_id": [101, 102, 103, 104, 105],
    "produto": [
        "Notebook",
        "Mouse",
        "Teclado",
        "Monitor",
        "Headset"
    ],
    "categoria": [
        "Eletrônicos",
        "Periféricos",
        "Periféricos",
        "Eletrônicos",
        "Periféricos"
    ],
    "preco": [3500.00, 80.00, 150.00, 1200.00, 250.00]
}

produtos = pd.DataFrame(dados_produtos)

produtos.to_csv(
    "data/raw/produtos.csv",
    index=False,
    encoding="utf-8"
)

print("Arquivo produtos.csv criado com sucesso!")
print(produtos)

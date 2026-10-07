import pandas as pd

arquivo = "data/raw/clientes.csv"

clientes = pd.read_csv(arquivo)

print("=== VALIDAÇÃO DOS CLIENTES ===")

erros = []

# Regra 1: verificar valores nulos
if clientes.isnull().sum().sum() > 0:
    erros.append("Existem valores nulos.")

# Regra 2: verificar duplicados
if clientes.duplicated().sum() > 0:
    erros.append("Existem registros duplicados.")

# Regra 3: verificar idade
if not clientes["idade"].between(0, 120).all():
    erros.append("Existem idades inválidas.")

# Regra 4: verificar estados
estados_validos = ["SP", "RJ", "MG", "PR", "SC", "RS", "ES", "BA"]

if not clientes["estado"].isin(estados_validos).all():
    erros.append("Existem estados inválidos.")

# Resultado
if len(erros) == 0:
    print("\nSTATUS: APROVADO")
    print("Todos os dados passaram nas validações.")
else:
    print("\nSTATUS: REPROVADO")
    print("\nErros encontrados:")

    for erro in erros:
        print(f"- {erro}")

import pandas as pd

# Define o número máximo de linhas para exibir
pd.set_option('display.max_rows', 71)

# Define o número máximo de colunas para exibir
pd.set_option('display.max_columns', 10)

# Lê o arquivo Excel
try:
    excel = pd.read_excel('grafico40.xlsx')
    print(excel)
except FileNotFoundError:
    print("Erro: Arquivo grafico40.xlsx não encontrado.")
except ImportError:
    print("Erro: Biblioteca openpyxl não encontrada. Instale-a com 'pip install openpyxl'.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

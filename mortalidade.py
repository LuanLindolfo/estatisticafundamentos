# Trabalho de estatística em Python
# Dados: Originados do acesso público https://www.ibge.gov.br/estatisticas/sociais/populacao/9109-projecao-da-populacao.html?edicao=41053
# e filtrados conforme as condições desejadas
# Tema: Esperança de vida de mulheres paraenses de 40 anos de idade entre  2000-2070

import pandas as pd# Para manipulação de dados em formato de tabela
import numpy as np# Para operações matemáticas e manipulação de arrays
import matplotlib.pyplot as plt  # Para criação de gráficos
import matplotlib.pyplot as plt# Para manipulação de dados em formato de tabela
from sklearn.utils import resample  # Para amostragem aleatória dos dados
from scipy import stats

#Um DataFrame é uma estrutura de dados bidimensional, organizada em linhas e colunas, que pode
#conter dados de tipos diferentes. É semelhante a uma planilha.


# Define o número máximo de linhas para exibir - 71 nesse caso
pd.set_option('display.max_rows', 71)

# Define o número máximo de colunas para exibir
pd.set_option('display.max_columns', 10)

# Lê o arquivo Excel
try:
    excel = pd.read_excel('grafico40.xlsx')
    print(excel)#exibe tudo (nesse caso, o tudo tá definido como 71)
    #print(excel.iloc[5]) #exibe somentea linha 6 (vetor começa do 0  )
except FileNotFoundError:
    print("Erro: Arquivo grafico40.xlsx não encontrado.")
except ImportError:
    print("Erro: Biblioteca openpyxl não encontrada. Instale-a com 'pip install openpyxl'.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

linhas = excel.shape[0]
colunas = excel.shape[1]

#quantidade de linhas e colunas
print(f"Quantidade de linhas: {linhas-1}")#-1 pois o vetor começa do 0 e está contando com a linha de cabeçalho
print(f"Quantidade de colunas: {colunas}")

#quantidade de linhas e colunas
#em excel há dois vetores (0 e 1) para referenciar as linhas e colunas respectivamente
#print(f"Quantidade de linhas: {excel.shape[0]}") - 0 são as linhas em excel
#print(f"Quantidade de colunas: {excel.shape[1]}") - 1 são as colunas em excel

#a soma de esperança
print(f"Soma de esperança: {excel['esperanca'].sum()}")
#excel[ acessa a coluna chamada "esperanca"
#.sum(): Este método é chamado na Series retornada no passo anterior. 
#Ele calcula a soma de todos os valores numéricos presentes na coluna "esperanca".
#

#media de esperança
media = excel['esperanca'].mean()
print(f"Média de esperança: {media:.2f}")
#excel[ acessa a coluna chamada "esperanca"
#.mean(): Este método é aplicado à Series obtida no passo anterior. 
#Ele calcula a média aritmética de todos os valores numéricos presentes na coluna "esperanca".


#mediana de esperança
mediana = excel['esperanca'].median()
print(f"Mediana de esperança: {mediana:.2f}")
#excel[ acessa a coluna chamada "esperanca"
#.median(): calcula a mediana de uma Series (coluna) ou de um DataFrame
#Ele calcula a mediana de todos os valores numéricos presentes na coluna "esperanca".

#moda de esperança
print(f"A lista é amodal, não possui moda (termo que mais se repete)")
#print(f"Moda de esperança: {excel['esperanca'].mode()}")
#excel[ acessa a coluna chamada "esperanca"
#.mode(): calcula a moda de uma Series ou de um DataFrame
#Ele calcula a moda de todos os valores numéricos presentes na coluna "esperanca".

#desvio padrão de esperança
dp = excel['esperanca'].std()
print(f"Desvio padrão de esperança: {dp:.2f}")
#excel[ acessa a coluna chamada "esperanca"
#.std():é usado para calcular o desvio padrão de uma série de dados
#Ele calcula o desvio padrão de todos os valores numéricos presentes na coluna "esperanca".


#declaração da variância
variancia=0

#para importar para .txt pra gerar o gráfico


# Extrai a coluna 'esperanca' como uma lista
#valores = excel['esperanca'].tolist()  # ou excel['esperanca'].values, se já for um array NumPy

# Cria um dicionário para armazenar todos os dados
dados_para_salvar = {
    'valores': excel['esperanca'].tolist(),
    'media': excel['esperanca'].mean(),
    'mediana': excel['esperanca'].median(),
    'desvio_padrao': excel['esperanca'].std()
}

# Converte o dicionário para um DataFrame
df_para_salvar = pd.DataFrame(dados_para_salvar)

# Salva o DataFrame em um arquivo CSV
df_para_salvar.to_csv('dados.csv', index=False)  # index=False evita salvar os números de linha

# Salva os valores em um arquivo de texto
#np.savetxt('dados.txt', np.array(valores).reshape(-1, 1), delimiter=',')


# Dados de exemplo (substitua pelos seus dados reais)
#dados = {
 #   'valores': [1, 2, 3, 4, 5],
 #   'media': 43.3352,
 #   'mediana': 43.5048,
 #   'moda': 0,
 #   'desvio_padrao': 2.5344
#}

# Salvar dados em um arquivo de texto
#np.savetxt('dados.txt', np.array(list(dados.values())), delimiter=',')

#valores, media, mediana, desvio_padrao = excel.iloc[:, 0:4].values.T  # Seleciona todas as colunas (índices 0 a 3) e tranforma em tupla
ano = excel.iloc[:, 3].values  # Seleciona a primeira coluna (índice 0)
esperanca = excel.iloc[:, 5].values  # Seleciona a segunda coluna (índice 1)

plt.plot(excel.index, excel['esperanca'], label='Esperança de Vida')



plt.xlabel("Tempo")  # Ou use o cabeçalho do Excel
plt.ylabel("Esperança de Vida")
plt.title("Gráfico dos dados")

plt.show()

#testando grafico aleatório
#x = [1, 2, 3, 4, 5]
#y = [2, 4, 1, 5, 3]

#plt.plot(x, y)
#plt.xlabel("Eixo X")
#plt.ylabel("Eixo Y")
#plt.title("Gráfico Simples")
#plt.show()


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

from sklearn.utils import resample

# Função para calcular estimadores de uma amostra
def calcular_estimadores(amostra):
    if amostra is None or len(amostra) == 0:
        raise ValueError("Amostra vazia")

    media = np.mean(amostra)
    variancia = amostra.var(ddof=1)
    dp = amostra.std(ddof=1)
    #mediana = amostra.median()
    mediana = np.median(amostra)


    try:
        #moda = amostra.mode().iloc[0]
        moda = stats.mode(amostra)[0][0]  
    except IndexError:
        moda = float('nan')

    return media, variancia, dp, mediana, moda

# Proporções das amostras (0.01%, 0.1%, 1%, 5%)
proporcoes = [0.0001, 0.001, 0.01, 0.05]

# Lista para armazenar os resultados das amostras
resultados = []

# Gerar amostras e calcular estimadores
#for prop in proporcoes:
  #  n = max(1, int(linhas * prop))
  #  if n > linhas:
  #      n = linhas
   # amostra = resample(esperanca, n_samples=n, replace=False, random_state=42)
   # media, variancia, dp, mediana, moda = calcular_estimadores(amostra)

    # Armazena os resultados em um dicionário
   # resultados.append({
    #    'Proporção': prop * 100,
    #    'Tamanho da amostra (n)': n,
    #   'Média': media,
      #  'Variância': variancia,
      #  'Desvio Padrão': dp,
       # 'Mediana': mediana,
      #  'Moda': moda
   # })

# Exibe os resultados das amostras em formato tabular
#resultados_df = pd.DataFrame(resultados)
#print("\nResultados das amostras:")
#print(resultados_df)

# Comparação com os parâmetros da população
##for idx, row in resultados_df.iterrows():
 #   print(f"\nAmostra de {row['Proporção']}% (n = {row['Tamanho da amostra (n)']}):")
 #   print(f"Média: {row['Média']:.2f} (População: {media:.2f})")
   # print(f"Variância: {row['Variância']:.2f} (População: {variancia:.2f})")
   # print(f"Desvio Padrão: {row['Desvio Padrão']:.2f} (População: {dp:.2f})")
   # print(f"Mediana: {row['Mediana']:.2f} (População: {mediana:.2f})")

   # moda = pd.Series(stats.mode(amostra)[0])
   # print(f"Moda: {row['Moda']} (População: {moda.iloc[0] if not moda.empty else 'N/A'})")




# Proporções das amostras (0.01%, 0.1%, 1%, 5%)


# Gerar amostras, calcular estimadores e plotar gráficos
#for i, prop in enumerate(proporcoes, start=1):
    #n = max(1, int(linhas * prop))
    #amostra = resample(esperanca, n_samples=n, replace=False, random_state=42)
    
    # Plotar a distribuição de frequência
   # plt.subplot(2, 2, i)  # Criar subplots 2x2
   # plt.hist(amostra, bins=30, alpha=0.7, color='b', edgecolor='black')
    #plt.title(f'Distribuição de Frequência\nProporção: {prop*100:.2f}%, n={n}')
    #plt.xlabel('Esperança de Vida')
    #plt.ylabel('Frequência')

#plt.tight_layout()
#plt.show()

    #xxxx
# Distribuição normal
#amostra_normal = np.random.normal(0, 1, n)
#plt.hist(amostra_normal, bins=30, alpha=0.5, label='Normal')

# Distribuição uniforme
#amostra_uniforme = np.random.uniform(-1, 1, n)
#plt.hist(amostra_uniforme, bins=30, alpha=0.5, label='Uniforme')

# Distribuição exponencial
#amostra_exponencial = np.random.exponential(1, n)
#plt.hist(amostra_exponencial, bins=30, alpha=0.5, label='Exponencial')

#plt.title('Comparação de Distribuições')
#plt.xlabel('Valores da Amostra')
#plt.ylabel('Frequência')
#plt.legend()
#plt.show()
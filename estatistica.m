#plot no octave
cd 'C:\Users\T-GAMER\OneDrive\Workspace\py'; # Muda para o diretório
dados = csvread('dados.csv'); # Agora leia o arquivo

# Ou, se preferir, use o caminho completo:
#dados = csvread('C:\Users\T-GAMER\OneDrive\Workspace\py\dados.csv'); #abrindo o arquivo .csv

#se a função "readtable" estivesse funcionando
#nomeando as variaveis dos valores agregados no .csv
#valores = dados.valores;
#media = dados.media;
#mediana = dados.mediana;
#desvio_padrao = dados.desvio_padrao;


#da função csvread - atribuindo as tabelas
# Como 'csvread' retorna uma matriz, precisará separar as colunas manualmente
valores = dados(:, 1);
media = dados(1, 2);  # Ajuste os índices conforme a posição da média no seu arquivo
mediana = dados(1, 3); # Ajuste os índices conforme a posição da mediana no seu arquivo
desvio_padrao = dados(1, 4); # Ajuste os índices conforme a posição do desvio padrão no seu arquivo

media = mean(valores);
mediana = median(valores);
desvio_padrao = std(valores);

# Cria um vetor com os índices das linhas
indices = 1:length(valores);

hist(valores); #pode gerar diferentes tipos de gráficos. Por exemplo, para criar um histograma dos valores, você pode usar a função hist:
plot(indices, valores);

# Extrai as colunas (ajuste os índices conforme a estrutura do seu arquivo)
valores = dados.valores; # Valores de esperança de vida
media = mean(valores); # Calcula a média
n_linhas = length(valores); # Número de linhas (71)


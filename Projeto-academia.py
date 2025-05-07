# 1. Importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 2. Carregar o dataset (ajuste o caminho se necessário)
diretorio = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(diretorio, 'academia_dados.csv')
df = pd.read_csv(csv_path)

# 3. Visualizar as primeiras linhas
print(df.head())

# 4. Informações gerais
print(df.info())
print(df.describe())

# 5. Análise Exploratória

# Quantidade de alunos por status
status_counts = df['Status'].value_counts()
print(status_counts)

# Gráfico de pizza do status
status_counts.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Ativos e Desistentes')
plt.ylabel('')
plt.show()

# Média de frequência semanal por status
freq_media = df.groupby('Status')['Frequência_Semanal'].mean()
print(freq_media)

# Gráfico de barras para média de frequência com valor no topo
ax = freq_media.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Média de Frequência Semanal por Status')
plt.ylabel('Frequência')

# Adiciona os valores no topo das barras
for i, v in enumerate(freq_media):
    plt.text(i, v + 0.05, f'{v:.2f}', ha='center')

plt.show()

# Motivos de desistência
motivos = df[df['Status'] == 'Desistente']['Motivo_Desistencia'].value_counts()
print(motivos)

# Gráfico de motivos com valores ao lado das barras
ax = motivos.plot(kind='barh', color='orange')
plt.title('Motivos de Desistência')
plt.xlabel('Quantidade')

# Adiciona os valores ao lado das barras
for i, v in enumerate(motivos):
    plt.text(v + 0.1, i, str(v), va='center')

plt.show()

# 6. Conclusões
# (Escreva aqui suas percepções)

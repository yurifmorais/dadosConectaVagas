import pandas as pd
#UF = RS
#CODIGO SM = 8841
#df = df.query("`CNAE 1` == 6202300 | `CNAE 1` == 4651601 | `CNAE 2` == 6202300 | `CNAE 2` == 4651601")

#filtrando por UF = RS
# df = pd.read_csv('estabelecimentos.estabele', encoding='ISO-8859-1', sep=';', low_memory=False)
# df = df.iloc[:, [0, 4, 5, 11, 12, 19, 20]]
# df.columns = ['CNPJ', 'NOME FANTASIA', 'SITUAÇÃO CADASTRAL', 'CNAE 1', 'CNAE 2', 'UF', 'Municipio']
# df = df.query("UF == 'RS'")
# print(df.head(1000))


#criando um novo arquivo com os dados filtrados
# df = pd.read_csv('estabelecimentos.ESTABELE', encoding='ISO-8859-1', sep=';', low_memory=False)
# df = df.iloc[:, [0, 4, 5, 11, 12, 19, 20]]
# df.columns = ['CNPJ', 'NOME FANTASIA', 'SITUAÇÃO CADASTRAL', 'CNAE 1', 'CNAE 2', 'UF', 'Municipio']
# df = df.query("UF == 'RS'")
# df.to_csv('dadosFiltrados.csv', index=False)
# print(df.head(1000))


#filtrando por CODIGO SM = 8841
#df = pd.read_csv('dadosFiltrados.csv', encoding='ISO-8859-1', sep=',', low_memory=False)
#df = df.query("Municipio == 8841")
#df.to_csv('dadosFiltrados.csv', index=False)
#print(df.head(1000))


#filtrando por CNAE 1 = 6202300 ou CNAE 1 = 4651601 ou CNAE 2 = 6202300 ou CNAE 2 = 4651601. ainda nao estou salvando a consulta
df = pd.read_csv('dadosFiltrados.csv', encoding='ISO-8859-1', sep=',', low_memory=False)
df = df.query("`CNAE 1` == 6202300 | `CNAE 1` == 4651601 | `CNAE 2` == 6202300 | `CNAE 2` == 4651601")
print(df.head(1000))
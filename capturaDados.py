import pandas as pd
#UF = RS
#CODIGO SM = 8841
#62.02-3-00 - Desenvolvimento e licenciamento de programas de computador customizáveis
#46.51-6-01 - Comércio atacadista de equipamentos de informática
#46.51-6-02 - Comércio atacadista de suprimentos para informática
#47.51-2-01 - Comércio varejista especializado de equipamentos e suprimentos de informática
#62.01-5-01 - Desenvolvimento de programas de computador sob encomenda
#62.01-5-02 - Web design
#62.01-5-03 - Desenvolvimento e licenciamento de programas de computador customizáveis
#62.01-5-04 - Desenvolvimento e licenciamento de programas de computador não-customizáveis
#62.01-5-05 - Suporte técnico, manutenção e outros serviços em tecnologia da informação


## filtrando por UF = RS
# df = pd.read_csv('estabelecimentos.estabele', encoding='ISO-8859-1', sep=';', low_memory=False)
# df = df.iloc[:, [0, 1, 2, 4, 5, 11, 12, 19, 20]]
# df.columns = ['CNPJ 1', 'CNPJ 2','CNPJ 3', 'NOME FANTASIA', 'SITUAÇÃO CADASTRAL', 'CNAE 1', 'CNAE 2', 'UF', 'Municipio']
# df = df.query("UF == 'RS'")
# print(df.head(1000))


#criando um novo arquivo com os dados filtrados pelo UF = RS
# df = pd.read_csv('estabelecimentos.ESTABELE', encoding='ISO-8859-1', sep=';', low_memory=False)
# df = df.iloc[:, [0, 1, 2, 4, 5, 11, 12, 19, 20]]
# df.columns = ['CNPJ 1', 'CNPJ 2','CNPJ 3', 'NOME FANTASIA', 'SITUAÇÃO CADASTRAL', 'CNAE 1', 'CNAE 2', 'UF', 'Municipio']
# df = df.query("UF == 'RS'")
# df.to_csv('dadosFiltrados.csv', index=False)
# print(df.head(1000))


#filtrando por CODIGO SM = 8841
# df = pd.read_csv('dadosFiltrados.csv', encoding='ISO-8859-1', sep=',', low_memory=False)
# df = df.query("Municipio == 8841")
# df.to_csv('dadosFiltrados.csv', index=False)
# print(df.head(1000))


#filtrando por CNAE 1 = 6202300 ou CNAE 1 = 4651601 ou CNAE 2 = 6202300 ou CNAE 2 = 4651601. ainda nao estou salvando a consulta
cnae_codes = [6202300, 4651601, 6200200, 4651602, 4751201, 6200101, 6200102, 6200103, 6200104, 6200105]
df = pd.read_csv('dadosFiltrados.csv', encoding='ISO-8859-1', sep=',', low_memory=False)
df = df[df['CNAE 1'].isin(cnae_codes) | df['CNAE 2'].isin(cnae_codes)]
df.to_csv('dadosFiltrados.csv', index=False)
print(df.head(1000))
import pandas as pd
from sqlalchemy import create_engine

# Carregar dados do CSV
df = pd.read_csv('dadosFiltrados.csv')

# Adicionar três zeros antes do valor na coluna CNPJ 2
df['CNPJ 2'] = df['CNPJ 2'].apply(lambda x: f'{x:04d}')

# Combinar colunas CNPJ sem espaços ou vírgulas
df['CNPJ'] = df[['CNPJ 1', 'CNPJ 2', 'CNPJ 3']].apply(lambda x: ''.join(x.dropna().astype(str)), axis=1)

# Combinar colunas CNAE
df['CNAE'] = df[['CNAE 1', 'CNAE 2']].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

# Renomear as colunas para corresponder às do banco de dados
df = df.rename(columns={'NOME FANTASIA': 'NOME_FANTASIA', 'SITUACAO CADASTRAL': 'SITUACAO_CADASTRAL'})

# Remover colunas antigas
df = df.drop(columns=['CNPJ 1', 'CNPJ 2', 'CNPJ 3', 'CNAE 1', 'CNAE 2'])

# Criar conexão com o banco de dados
engine = create_engine('mysql://root:root@localhost/conectavagas')

# Inserir dados na tabela company
df.to_sql('company', con=engine, if_exists='append', index=False)

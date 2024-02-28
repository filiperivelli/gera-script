import pandas as pd

def gerar_comandos_insert(nome_arquivo):
    # Lê o arquivo Excel, considerando a segunda linha como cabeçalho
    df = pd.read_excel(nome_arquivo, header=1)
    
    # Nome da tabela (você pode ajustar conforme necessário)
    nome_tabela = input("Digite o nome da tabela:")

    # Obtém os nomes das colunas
    colunas = df.columns.tolist()

    # Itera sobre as linhas e gera os comandos INSERT
    for index, row in df.iterrows():
        valores = ", ".join([f"'{str(row[coluna])}'" for coluna in colunas])  # Assume que todos os valores são strings
        comando_insert = f"INSERT INTO {nome_tabela} ({', '.join(colunas)}) VALUES ({valores});"
        print(comando_insert)

# Chamada da função com o nome do arquivo Excel como argumento
gerar_comandos_insert('PlanilhaTeste.xlsx')
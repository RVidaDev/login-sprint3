import pandas as pd

# Função para ler o CSV e converter em uma lista de dicionários
def csv_to_list_of_dicts(file_path):
    try:
        # Lê o arquivo CSV e converte em um DataFrame
        df = pd.read_csv(file_path, error_bad_lines=False)
        
        # Converte o DataFrame em uma lista de dicionários
        data_list = df.to_dict(orient='records')
        
        return data_list
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []
    except pd.errors.ParserError:
        print("Erro ao analisar o arquivo CSV.")
        return []

# Exemplo de uso
file_path = 'seu_arquivo.csv'
data = csv_to_list_of_dicts(file_path)
print(data)
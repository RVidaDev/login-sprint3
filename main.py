from pathlib import Path

# Função para ler o CSV e converter em uma lista de dicionários
def csv_pra_dict(caminho):
    try:
        with Path(caminho).open() as file:
            #nomes_coluna vai ler o nome da coluna, tirar espaços em ranco -
            # e separar cada elemento corretamente usando virgula como separador
            # ATENÇÂO pode não ser esse separador no csv
            nomes_coluna = file.readline().strip().split(",")
            data_list = []
            for linha in file:
                #vai ler uma linha e dividir a linha em campos como se fosse uma lista de string
                field = linha.strip().split(",")
                #cria um dicionário pra cada linha
                linha_dict = {nomes_coluna[i]: field[i] for i in range(len(nomes_coluna))}
                data_list.append(linha_dict)
        return data_list
    
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao analisar o arquivo CSV: {e}")
        return []
            
    
# Exemplo de uso
<<<<<<< HEAD
file_path = Path('login-sprint3\click.csv')
data = csv_pra_dict(file_path)
=======
file_path = 'arquivo.csv'
data = csv_to_list_of_dicts(file_path)
>>>>>>> 00dee12e3cbc01181a437cd3439b9df9e619f3fd
print(data)
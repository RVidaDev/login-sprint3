import csv

def ler_csv(file):
    try:
        with open(arquivo_csv, 'r') as arquivo:
            leitor = csv.DictReader(arquivo)
            dados = [dict(linha) for linha in leitor_csv]
        return dados
    except FileNotFoundError:
        print(f"O arquivo '{arquivo_csv}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")
        return []


def main():
   
            
if __name__ == "__main__":
    main()
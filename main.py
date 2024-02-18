
usuarios = []

def cadastrar_usuario():
    nome = input("Digite o Nome: ")
    email = input("Digite seu email: ")
    
    for usuario in usuarios:
        if usuario['nome'] == nome or usuario['email'] == email:
            print("Usuário já cadastrado.")
            return
    
    usuarios.append({'nome': nome, 'email': email})
    print(f"cadastro de {nome} realizado com sucesso.")
    
def listar_usuarios():
    for usuario in usuarios:
        print("Cadastro: ")
        print(f"Nome: {usuario['nome']}, Email: {usuario['email']}")

def main():
    while True:
        
        print("\nOpção 1: cadastrar usuário")
        print("Opção 2: Listar Usuários")
        print("opção 3: Sair")
        
        opcao = input("Escolha a opção desejada: ").lower()
        
        match opcao:
            case "1":
                cadastrar_usuario()
            case "2":
                listar_usuarios()
            case "3":
                print("Encerrando cadastro.")
                break
            
if __name__ == "__main__":
    main()
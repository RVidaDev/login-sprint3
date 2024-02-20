from getpass import getpass

usuarios = []

def cadastrar_usuario():
    try:
        nome = input("Digite o Nome: ")
        email = input("Digite seu email: ")
        
        if "@" not in email:
            raise ValueError("O email do usuário não é válido.")
        
        senha = getpass(prompt="digite sua senha: ")
        confirmSenha = getpass(prompt="confirme sua senha: ")    
        
        if senha == confirmSenha:
            print("Senha cadastrada!")
        else:
            print("As senhas estão diferentes! Tente novamente")
            return
            
        
        for usuario in usuarios:
            if usuario['nome'] == nome or usuario['email'] == email:
                print("Usuário já cadastrado.")
                return
        
        usuarios.append({'nome': nome, 'email': email})
        print(f"cadastro de {nome} realizado com sucesso.")
        
    except ValueError as erro:
        print("Erro:", erro)
        
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
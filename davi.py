"""Enunciado:
Utilizando o menu a baixo, desenvolva o código necessário conforme
as instruções:

Na opção 1, você deverá 'cadastrar' o login e a senha de uma pessoa.
    Obs: - Você deverá realizar a confirmação da senha antes de 
            salvar na lista de senhas (lst_senhas) e na lista de logins 
            (lst_logins).
            Caso as duas senhas não sejam iguais, avisar o usuário e permitir
            a digitação novamente da senha e novamente a confirmação.
        - Permita apenas 3 tentativas. Volte ao Menu.
        - O login deve ser único, a senha pode repetir.

Na opção 2, você deverá testar se o login e a senha estão funcionando
    corretamente. Se estiver, avise que está tudo ok. 

Na opção 3, você deverá possibilitar a troca de senha de um usuário.
    Para isso, leia o login, e a senha antiga. 
    Se estiver OK, aceite a nova senha. 
    Obs: Não esqueça de validar novamente a senha.
    
Na opção 4, você deverá implementar a exclusão de um login e também 
    da senha correspondente. 
    
"""

# Sua tarefa é desenvolver o que falta no código abaixo.

menu = """
           CADASTRE SEU LOGIN
    ================================
    0- Finaliza o código
    1- Cadastrar login e senha
    2- Validar login e senha
    3- Alterar a senha
    4- Excluir um login
    5- Mostrar logins
    ================================
"""
    
lst_logins = []
lst_senhas = []

while True:
    print(menu)
    escolha = input("    Escolha: ")

    if escolha == "0":
        print("FInalizando codigo...")
        break

    if escolha == "1":
        login = input("Digite seu login:")
        if login in lst_logins:
            print("Este login ja existe, tente novamente!")
            continue
        senha = input("Escolha sua senha:")
        confirmaçao =  input("COnfirme sua senha:")
        tentativas = 0 
        while senha != confirmaçao and tentativas < 3:
            print ("Senhas nao identicas, tente novamente com a mesma senha utilizada!")
            senha = input("Digite novamente sua senha:")
            confirmaçao = input("Confirme novamente sua senha:")
            tentativas += 1
        if tentativas == 3:
            print("Numero exedito de tentativas, votando pro menu")
            continue    
        lst_logins.append(login)
        lst_senhas.append(senha)
        print("Login e senha cadastrados com sucesso!")

    if escolha == "2":
        login = input("Digite seu login:")
        senha = input("Digite sua senha:")
        if login in lst_logins and senha in lst_senhas:
            print("Acesso concedido, login verificado.")
        else:
            print("Login nao verificado, crie um ou tente novamente.")

    if escolha == "3":
            login = input("Digite seu login:")
            if login not in lst_logins:
                print("Login nao existe, cadastre-se ")
                continue
            senha_antiga = input ("Digite sua senha antiga:")
            if senha_antiga not in lst_senhas[lst_logins.index(login)]:
               print("Senha errada")
               continue
            senha_nova = input("Digite a nova senha: ")
            confirmacao = input("Confirme a nova senha: ")
            tentativas = 0
            while senha_nova != confirmacao and tentativas < 3:
                print("Senhas não conferem! Tente novamente.")
                senha_nova = input("Digite a nova senha: ")
                confirmacao = input("Confirme a nova senha: ")
                tentativas += 1
            if tentativas == 3:
                print("Número de tentativas excedido! Tente novamente mais tarde.")
                continue
            lst_senhas[lst_logins.index(login)] = senha_nova
            print("Senha alterada com sucesso!")           
            

    if escolha == "4":
        while True:
            logar = input("Digite seu login:")
            senha = input("Digite sua senha:")
            if logar not in lst_logins:
                print("login errado")

            if senha not in lst_senhas:
                print("senha nao cadastrada")
                
            while senha in lst_senhas and logar in lst_logins:
                input("Você realmente deseja apagar? (s/n)")
                response = input().lower()  
                if response == 's':
                    lst_logins.remove(logar)
                    lst_senhas.remove(senha)
                    print("Login APAGADO")
                    break
                if response == 'n':
                    print("Operação cancelada.")
            break
            
    if escolha == "5":
        senhas = input("Digite a senha master(senha:master):")
        if senhas == "master":
            print(lst_logins)
            print(lst_senhas)

        else:
            print("Senha incorreta!!")
            continue
    
        
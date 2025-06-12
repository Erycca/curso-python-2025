
texto = """
Escolha a sua água para comprar
(1)Água mineral Natural
(2)Água mineral com gás
"""

opcao = input(texto)

if opcao == "1":
    print("Sua conta deu : R$ 1,50")

elif opcao == "2":
    print("Sua conta deu : R$ 2,50")

else: 
    print("Opção Invalida")
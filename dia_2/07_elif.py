# %%
texto = """
   Escolha sua água para comprar 
   (1) Agua mineral natural 
   (2) Agua mineral com gas
"""

opcao = input(texto)

valor_item = 0

if opcao == "1":
   valor_item ==1.5
elif opcao == "2":
    valor_item = 2.5

if valor_item == 0:
     print("Entre com a opção correta")
    
else:

     qtde = input("Quantas garrafas ?")
     qtde = int (qtde)
     valor_total = valor_item * qtde
      
     print("Sua conta é R$: ",   valor_total)

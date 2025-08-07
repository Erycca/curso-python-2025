numero_sorteio = 7

for i in range(3):
        
     while True:
        try:
            numero_usuario = int(input("Entre com um número:  "))

        except ValueError as err:
            print("Valor Invalido!")  
            continue


        if not 1 <= numero_usuario <= 15:
            print("Parabêns!!")
            continue

        if numero_sorteio == numero_usuario:
            print("Parabêns!!")
            break

        elif numero_usuario >numero_sorteio:
            print("Numero muito alto. Tente um numero menor!")

        else:
            print("Numero muito baixo. Tente um numero maior!")   

else:
     print("Suas tentativas acabaram !!")        
def par_impar(numero:int):
    if numero % 2 == 0:
       return "par"
    else:
        return "impar"
    
    numero = input("Entre com o numero:   ")
    numero = int(numero)

    resultado = par_impar(numero)

    print("O valor", numero, "é", resultado) 
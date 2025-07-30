def soma(a:float, b:float)->float:
    return a + b

def  media(a:float, b:float)->float:
    return soma(a,b) / 2 

a = float(input("entre com o valor de a: ")) 
b = float(input("entre com o valor de b: ")) 

print("Media: " , media(a,b))
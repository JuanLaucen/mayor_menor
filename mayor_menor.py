lista_numeros=[]
salir=0
try:
    
    for i in range(10):
        numero=int(input("Ingrese numero"))
        lista_numeros.append(numero)
    lista_numeros.sort(reverse=True)
    print("aqui esta su lista de numeros ordenada de mayor a menor \n" ,lista_numeros)
except:
    print("valor invalido")
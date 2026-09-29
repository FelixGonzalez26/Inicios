def validar_numero():
    
    while True:
        num= input("Ingrese un numero valido: ")
        try:
            if num.isdigit() and int(num) >0:
                return int(num)
            else:
                print("Ingrese un numero mayor a 0")

        except ValueError:
            print("No se permiten letras")

def analizador():
    rango= validar_numero()
    numeros=[]

    for i in range(rango):
        numeros.append(validar_numero())

    numero_alto= max(numeros)
    print(numero_alto)
    numero_menor = min(numeros)
    print(numero_menor)
    promedio= sum(numeros)/rango
    print(promedio)
    print(numeros)

analizador()
def validar_numero():
    
    while True:
        try:
            num= input("Ingrese un numero valido: ")
            if num.isdigit() and int(num) >0:
                return int(num)

        except ValueError:
            print("No se permiten letras: ")
"""
def num_list():
    while True:
        try:
            num = input("Ingrese un numero (puede ser negativo): ")
            return int(num)  # El try atrapa las letras automáticamente
        except ValueError:
            print("No se permiten letras.")
"""

def clasificar_list():
    rango= validar_numero()
    list1=[]
    listpos=[]
    listneg=[]
    numeros=0
    count_pos=0
    count_neg=0

    for i in range(rango):
        numeros= validar_numero()
        list1.append(numeros)
        if numeros %2==0 :
            listpos.append(numeros)
            count_pos+=1
            
        else:
            listneg.append(numeros)
            count_neg+=1

    print(f"La lista principal es: {list1}")
    print(f"La lista Par es: {listpos}")
    print(f"La lista Impar es: {listneg}")

    return count_pos, count_neg

count1, count2= clasificar_list()
print(f"\n--- RESULTADOS COUNT ---")
print(f"El total de numeros pares fue: {count1}")
print(f"El total de numeros impares fue: {count2}")


     



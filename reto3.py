def validar_num():

    while True:
     num= input("Introduzca el numero: ")
     try:
         if num.isdigit() and int(num) >0:
            return int(num)
         else:
            print("Ingrese un numero mayor a 0")


     except ValueError:
      print("No se permiten letras")

def validar_datos():
     while True:
        num= input("Introduzca el numero: ")
        try:
            
         return int(num)
           
   
   
        except ValueError:
         print("No se permiten letras")

def suma_selectiva():
   print("Intrdouzca el rango de numeros: ")
   rango= validar_num()
   suma_total=0
   count=0
   
   for i in range(rango):
      print("Ingrese un numero: ")
      i=validar_datos()
      if i > 0:
         suma_total= suma_total+i
      else:
         count +=1
   return suma_total, count
   
   

total_suma, total_ignorados = suma_selectiva()

# Imprimimos el resultado formateado exactamente como querías
print(f"\n--- RESULTADOS FINALES ---")
print(f"La suma total de los numeros positivos fue: {total_suma}")
print(f"La cantidad de numeros negativos/ceros ignorados fue: {total_ignorados}")
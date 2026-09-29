
def validar():
    while True:
      num=input("Ingrese un numero valido: ")
      try:
         if num.isdigit() and int(num) >0:
            return int(num)
         else:
            print("Ingrese un numero mayor a 0")


      except ValueError:
        print("No se permiten letras")

def Tabla_filtrada():
   num=validar()
   num_par=0
   num_inpar=0

   for i in range(1,11):
      num_par= i*num
      if num_par %2==0:
         print(f"El numero par de la multiplicacion es: {num_par}")
      if num_par %2 !=0:
         num_inpar+=1

   return num_inpar

print(Tabla_filtrada())
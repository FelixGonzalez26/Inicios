
def validar_numero():
 while True:
  numero = input("Ingrese un numero: ")
  try:
    if numero.isdigit() and int(numero) >0 and int(numero) %2==0: 
     return numero
    
    

    else:
     print("solo se permiten numeros mayores a 0")
  except ValueError:
   print("No se permiten letras")



def recorrido_inverso():
 num= validar_numero()
 
 num= int(num)
 count=0
 for i in range (num, 0, -1):
  if i %2==0:
      print(i)
  else:
     count +=1

 return count
 

print(recorrido_inverso())
 



# miselania
menu = int(input("MENU PRINCIPAL\n\nElige el número que deseas realizar:\n\n1.Calcular el área de un triangulo.\n2.Ingresar dos números y realizar suma.\n3.Ingresar un numero y elevarlo al cuadrado.\n4.Realizar la suma de los números 1234 y 532.\n5.Realizar la resta de los números 1234 y 532.\n6.Realizar la multiplicación de los números 1234 y 532.\n7.Realizar la división de los números 1234 y 532.\n8.Modulo de los números 1234 y 532.\n9.Convertir euros a dólares.\n10.Calcular el area de un rectangulo.\n11.Calcular el area y perimero de un cuadrado.\n12.Calcular el área y volumen de un cilindro.\n13.Calcular el area y longitud de una circunferencia.\n14.Calcular el promedio de 3 números.\n"))
print("")
print ("LA OPRERACIÓN ESCOGIDA ES :",menu)
print("")
if menu ==1:
  print ("calcular el área de un triángulo")
  print("")
  base = int(input("Ingrese la base del triángulo: "))
  altura = int(input("Ingrese la altura del triángulo: "))
  area = (base * altura) / 2
  print("")
  print("El area del triangulo es:" , area )
elif menu ==2:
  print ("ingresa dos numeros para sumar")
  print("")
  num_1 = int(input("Ingrese el primer número: "))
  num_2 = int(input("Ingrese el segundo número: "))
  suma = num_1 + num_2
  print("")
  print("RESPUESTA:",suma )
elif menu==3:
  print ("elevar un número al cuadrado")
  num_1 = int(input("Ingrese el número: "))
  operacion= num_1 ** 2
  print("")
  print ("RESPUESTA:" ,operacion)
elif menu ==4:  
  print ("Este programa sumara los siguientes números 1234 y 532")
  print("")
  num_1 = 1234
  num_2 = 532
  print("")
  suma = num_1 + num_2
  print ("respuesta:",suma)
elif menu ==5:
  print ("Este programa restara los números 1234 y 532")
  print("")
  num_1 = 1234
  num_2 = 532
  print("")
  resta = num_1 - num_2
  print ("respuesta: ",resta)
elif menu ==6:
  print ("Este programa multiplicara los números números 1234 y 532")
  print("")
  num_1 = 1234
  num_2 = 532
  print("")
  multi = num_1 * num_2
  print ("respuesta:", multi)
elif menu ==7:
  print ("Este programa dividira los siguientes números 1234 y 532")
  print("")
  num_1 = 1234
  num_2 = 532
  div = num_1 / num_2
  print("")
  print ("respuesta:",div)
elif menu ==8:
  print ("Este programa hallara el modulo de los números 1234 y 532")
  print("")
  num_1 = 1234
  num_2 = 532
  div = num_1 % num_2
  print("")
  print ("respuesta:" ,div)
elif menu ==9:
  print ("cambio de euros a dolares")
  print("")
  euro = float(input("Ingrese la cantidad de euros a cambiar: "))
  dolar = 0.911202
  conv = euro / dolar
  print("")
  print (f"La cantidad de {euro} euros coresponde a : {conv} dolares")
elif menu ==10:
  print ("calcular el área de un rectangulo")
  print("")
  ancho = float(input("Ingrese la medida del ancho del rectangulo: "))
  largo = float(input("Ingrese la medida de altura del rectangulo: "))
  print("")
  area = ancho * largo
  print("")
  print ("respuesta", area )
elif menu ==11:
  print ("Este programa calculara el área y el perimetro de un cuadrado")
  print("")
  lado = int(input("Ingrese la medida del lado del cuadrado: "))
  area = lado * lado
  per = lado + lado + lado + lado
  print("")
  print (f"El área del cuadrado es: {area} y su perimetro es {per} ")
elif menu ==12:
  print ("Este programa calculara el área y volumen de un cilindro:")
  print("")
  radio = int(input("Ingrese la medida del radio del cilindro: "))
  altura = int(input("Ingrese altura del cilindro: "))
  pi = 3.1416
  volumen = (pi * radio ** 2) * altura
  perimetro = (2 * pi * radio)
  area_1= perimetro * altura
  area = (2 * radio ** 2) * pi + area_1
  print("")
  print("")
  print (f"El volumen del cilindro es: {volumen} y su area es {area} ")
elif menu ==13:
  print ("Este programa calculara el area y la longitud de una circunferencia ")
  print("")
  radio = int(input("Ingrese la medida del radio de la circunferencia: "))
  pi = 3.1416
  diametro = 2 * radio
  longitud = diametro * pi
  area = pi * radio ** 2
  print("")
  print("")
  print (f"Longitud de la circunferencia: {longitud} y su area corresponde: {area}")
elif menu==14:
  print ("Este programa calculara el promedio de tres números")
  print("")
  n1 = int(input("Ingrese el primer número: "))
  n2 = int(input("Ingrese el segundo número: "))
  n3 = int(input("Ingrese el tercer número: "))
  promedio = (n1 + n2 + n3) / 3
  print("")
  print (f"El promedio de los números ingresados es : {promedio}")
else:
  print ("Ingresa un número del 1 al 14")
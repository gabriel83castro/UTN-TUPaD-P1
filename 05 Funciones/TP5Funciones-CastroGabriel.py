import math
# Actividad 1
"""Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""

"""def imprimir_hola_mundo(mensaje):
  print(mensaje)

imprimir_hola_mundo("Hola Mundo!") """

# Actividad 2
"""Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
"""

"""def saludar_usuario(nombre):
  print(f"Hola {nombre}!")

saludar_usuario("Marcos") """

# Actividad 3
"""
Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
"""

def informacion_personal(nombre,apellido,edad,residencia):
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
edad=input("ingrese su edad: ")
residencia=input("ingrese su residencia: ")
informacion_personal(nombre,apellido,edad,residencia)
"""
# Actividad 4

"""Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el 
radio al usuario y llamar ambas funciones para mostrar los resultados."""

"""
def calcular_area_circulo(radio):
  return math.pi * (radio**2)

def calcular_perimetro_circulo(radio):
  return 2 * math.pi * radio

radio = float(input("ingrese el radio: "))
print(f"El area del circulo es: {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")"""

# Actividad 5

"""Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función."""

"""
def segundos_a_horas(segundos):
  return segundos/3600

seg=float(input("ingrese los segundos: "))
print(f"Los {seg} segundos equivalen a {segundos_a_horas(seg)} horas")"""

# Actividad 6

"""Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función."""


"""def tabla_multiplicar(mensaje):
  num=int(input(mensaje))
  for i in range(1,11):
    print(f"{i} x {num} = {i*num}")
    

tabla_multiplicar("ingrese un numero: ")"""

# Actividad 7

"""Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""

"""def operaciones_basicas(a,b):
  while b == 0:
    b=float(input("ingrese un numero distinto de cero: "))
  return (a+b, a-b, a*b, a/b)

numero1=float(input("Por favor, ingrese un número: "))
numero2=float(input("Por favor, ingrese otro número: "))
print(operaciones_basicas(numero1,numero2))"""

# Actividad 8

"""Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""

"""def calcular_imc(peso,altura):
  return peso/(altura**2)

peso=float(input("Por favor, ingrese su peso en kg: "))
altura=float(input("Por favor, ingrese su altura en metros: "))
print(f"Su Indice de Masa Corporal (IMC) es: {calcular_imc(peso,altura)}")"""

# Actividad 9

"""Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función."""


"""def celsius_a_fahrenheit(celsius):
  return celsius * 1.8 + 32

temp=float(input("Temperatura en grados Celsius: "))
print(f"La temparatura en Fahrenheit es: {celsius_a_fahrenheit(temp)} °F")"""

# Actividad 10

"""Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta función."""

"""def calcular_promedio(a, b, c):
  return (a+b+c)/3

numero1=float(input("Ingrese un número: "))
numero2=float(input("Ingrese un número: "))
numero3=float(input("Ingrese un número: "))
print(f"El promedio de los números ingresados es: {calcular_promedio(numero1,numero2,numero3)}")"""
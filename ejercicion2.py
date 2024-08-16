"""
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.
"""

##############################################################################################################################################

"Operadores aritméticos"

#Se declaran las variables que se utilizaran.
num1 = 8
num2 = 5

#Se crea ejemplos de los operadores aritméticos. 
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
divisionEntera = num1 // num2
residuo = num1 % num2
exponenciacion = num1 ** num2

print("Números para el ejemplo:", num1, "y", num2)

#Se imprime por consola el resultado de las operaciones.
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", divisionEntera)
print("Residuo:", residuo)
print("Exponenciación:", exponenciacion, "\n") #Se añade "\n" para que haga un salto de línea.

##############################################################################################################################################

"Operadores de comparación"

#Se declaran las variables que se utilizaran.
num3 = 2
num4 = 10

print("Números para el ejemplo:", num3, "y", num4)

#Se crea ejemplos de los operadores de comparación.
print("Igualdad:", num3 == num4)
print("Diferente:", num3 != num4)
print("Mayor que:", num3 > num4)
print("Menor que:", num3 < num4)
print("Mayor o igual que:", num3 >= num4)
print("Menor o igual que:", num3 <= num4, "\n")

##############################################################################################################################################

"Operadores lógicos"

#Se declaran las variables que se utilizaran.
num5 = 7
num6 = 14

print("Números para el ejemplo:", num5, "y", num6)

#Se crea ejemplos de los operadores de lógicos.
print("¿7 es mayor que 5 y 14 es menor que 20?:", num5 > 5 and num6 < 20) #Se utiliza "and" si ambas condiciones son verdaderas.
print("¿7 es mayor que 10 o 14 es menor que 16?:", num5 > 10 or num6 < 16) #Se utiliza "or" si al menos una condición es verdadera.
print("¿14 es menor que 10?:", not(num6 < 10), "\n") #Se utiliza not() para invertir el valor lógico.

##############################################################################################################################################

"Operadores de asignación"

#Se declaran las variables que se utilizaran.
num7 = 50 #Asigna un valor a una variable.
num8 = 25
num9 = 92
num10 = 30
num11 = 60

print("Números para el ejemplo:", num7, ",", num8, ",", num9, ",", num10, "y", num11)

#Se crea ejemplos de los operadores de lógicos.
num8 += 10 #Se incrementa el valor de una variable.
num9 -= 47 #Se decrementa el valor de una variable.
num10 *= 3 #Se multimipla el valor de una variable.
num11 /= 2 #Se divide el valor de una variable.

#Se imprime por consola el resultado de las operaciones.
print("Se asigna un valor a una variable (a = 50):", num7)
print("Se incrementa el valor de una variable (25 + 10):", num8)
print("Se decrementa el valor de una variable (92 - 47):", num9)
print("Se multiplica el valor de una variable (30 * 3):", num10)
print("Se divide el valor de una variable (60 / 2):", num11, "\n")

##############################################################################################################################################

"Operadores de identidad"

#Se declaran las variables que se utilizaran.
num12 = [10, 15, 25, 40]
num13 = num12 #La variable "num13" apunta a la variable "num12".
num14 = [11, 16, 26, 41]

print("Lista de números para el ejemplo:", num12, ",", num13, "y", num14)

#Se imprime por consola el resultado de las operaciones.
print("¿num12 y num13 están apuntando al mismo objeto?:", num12 is num13)
print("¿num12 y num14 no están apuntando al mismo objeto?:", num12 is not num14, "\n")

##############################################################################################################################################

"Operadores de pertenencia"

#Se utilizaran las variables que se utilizaron en el anterior ejemplo.
print("Lista de números para el ejemplo:", num12, "y", num14)

#Se imprime por consola el resultado de las operaciones.
print("¿El numero 25 esta en la lista?:", 25 in num12)
print("¿El numero 50 esta en la lista?:", 50 in num12)
print("¿El numero 20 no esta en la lista?:", 20 not in num14)
print("¿El numero 41 no esta en la lista?:", 41 not in num14, "\n")

##############################################################################################################################################

"Operadores de bits"

#Se declaran las variables que se utilizaran.
num15 = 6
num16 = 3

print("Lista de números para el ejemplo:", num15, "y", num16)

#Se imprime por consola el resultado de las operaciones.
print("Devuelve 1 solo si ambos bits son 1:", num15 & num16)
print("Devuelve 1 solo si al menos un bit es 1:", num15 | num16)
print("Devuelve 1 si los bits son diferentes:", num15 ^ num16)
print("Desplaza los bits hacia la izquierda:", num15 << 1)
print("Desplaza los bits hacia la izquierda:", num15 >> 1, "\n")

##############################################################################################################################################

"Estructuras de control en Python"

"Estructuras condicionales"
#Se declaran las variables que se utilizaran.
num17 = 46
num18 = 27
num19 = 46

print("Lista de números para el ejemplo:", num17, ",", num18, "y", num19)

#Se imprime por consola el resultado de las operaciones.
if num17 > num18:
    print("El numero", num17, "si es mayor que 27")

if num18 < num17:
    print("El numero", num18, "no es mayor que 46")
else:
    print("El numero", num17, "si es mayor que 27")

if num17 > num19:
    print("El numero", num17, "si es mayor que 46")
elif num17 < num19:
    print("El numero", num17, "no es mayor que 46")
else:
    print("El numero a:", num17, "es igual al numero b:", num19, "\n")

##############################################################################################################################################

"Estructuras iterativas"

#Se declaran las variables que se utilizaran.
num20 = 7

print("Número para el ejemplo:", num20)

#La estructura "for" itera sobre una secuencia (como una lista o rango).
for i in range(5): # 0 a 4
    #Se imprime por consola el resultado de la operacion.
    print(i)

print() #Salto de linea.

#La estructura "while" repite el bloque mientras la condición sea verdadera.
while num20 < 14:
    #Se imprime por consola el resultado de la operacion.
    print(num20)
    num20 += 1

print() #Salto de linea.

##############################################################################################################################################

"Manejo de excepciones"

#Se declaran las variables que se utilizaran.
num21 = 5

print("Número para el ejemplo:", num21)


try:
    resultado = num21 / 0
    #Se imprime por consola el resultado de la operacion, y si ocurre una excepción, ejecuta el bloque "except".
except ZeroDivisionError:
    print("No se puede dividir por cero")

try:
    resultado = num21 / 0
    #Se imprime por consola el resultado de la operacion sin importar si ocurrió una excepción o no.
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Esto siempre se ejecuta:", num21)

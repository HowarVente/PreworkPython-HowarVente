"""
1. Dado un número, imprime si es positivo o negativo.
2. Dado un número, imprime si es par o impar.
3. Dado tres números, encuentra y muestra el mayor de ellos.
"""
numero = - 20
if numero > 1:
 print ("positivo")
else:
  print ("negativo") 
numero = 8
if numero % 2 == 0:
  print ("par")
else:
  print ("impar")
a,b,c =  18, 2, 33
mayor = max (a,b,c)
print (mayor)
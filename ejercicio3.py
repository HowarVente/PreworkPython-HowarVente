""""
1. Imprime los números del 1 al 10 usando un bucle for 
2. Imprime los números pares del 1 al 20 usando un bucle while 
3. Usa un bucle para calcular la suma de los números del 1 al 100.
"""
for i in range (1,10):
    print (i)
i = 1
while i <= 20 :
    if i  % 2 == 0 :
     print (i) 

suma = 0 
for i in range (1,101):
 suma += i
 print (suma) 
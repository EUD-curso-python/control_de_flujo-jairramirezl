
"""Guarde en lista `naturales` los primeros 100 números naturales (desde el 1) 
usando el bucle while
"""
n=0
naturales=list()
while n<100:
  naturales.append(n+1)
  n+=1
#print(naturales)
  
"""Guarde en `acumulado` una lista con el siguiente patrón:

['1','1 2','1 2 3','1 2 3 4','1 2 3 4 5',...,'...47 48 49 50']

Hasta el número 50.
"""
acumulado=list()
n=1
item=''
for i in range(1,51,1):
    tmp=list()
    while n<=i:
        #print(n,c)
        tmp.append(str(n))
        item=' '.join(tmp)
        n=n+1
    acumulado.append(item)    
    n=1
print(acumulado)


"""Guarde en `suma100` el entero de la suma de todos los números entre 1 y 100:
"""
suma100=0
for i in range(101):
  suma100+=i





"""Guarde en `tabla100` un string con los primeros 10 múltiplos del número 134, 
separados por coma, así:

'134,268,...'

"""
n=1
control=1
tabla100=''
l1=list()
while control <= 10:
    if n % 134 == 0:
        control+=1
        l1.append(str(n))
    n+=1        
tabla100=','.join(l1)






"""Guardar en `multiplos3` la cantidad de números que son múltiplos de 3 y 
menores o iguales a 300 en la lista `lista1` que se define a continuación (la lista 
está ordenada).
"""
lista1 = [12, 15, 20, 27, 32, 39, 42, 48, 55, 66, 75, 82, 89, 91, 93, 105, 123, 132, 150, 180, 201, 203, 231, 250, 260, 267, 300, 304, 310, 312, 321, 326]

acu=1
multiplos3=0
for i in lista1:
    if i % 3 == 0 and i<300:
      multiplos3=acu+multiplos3



"""Guardar en `regresivo50` una lista con la cuenta regresiva desde el número 
50 hasta el 1, así:

[
  '50 49 48 47...',
  '49 48 47 46...',
  ...
  '5 4 3 2 1',
  '4 3 2 1',
  '3 2 1',
  '2 1',
  '1'
]
"""

l1=list()   
l2=list()
regresivo50=list()  
n=1
for i in range(50,0,-1):
    while n<=i:
        l1.append(str(n))
        n=n+1
    l1.reverse()
    l2=' '.join(l1)
    regresivo50.append(l2)
    l1=list()    
    n=1 




"""Invierta la siguiente lista usando el bucle for y guarde el resultado en 
`invertido` (sin hacer uso de la función `reversed` ni del método `reverse`)
"""
lista2 = list(range(1, 70, 5))
invertido=list()
ll=len(lista2)-1
for i in lista2:
    invertido.append(lista2[ll])
    ll-=1



"""Guardar en `primos` una lista con todos los números primos desde el 37 al 300
Nota: Un número primo es un número entero que no se puede calcular multiplicando 
otros números enteros.
"""

primos=[]
count=0
for dig in range(37, 300+1):
    for dig_2 in range(1, dig + 1):
        if dig%dig_2==0:
            count+=1
    if count==2:
        primos.append(dig)
    count=0
print(primos)








"""Guardar en `fibonacci` una lista con los primeros 60 términos de la serie de 
Fibonacci.
Nota: En la serie de Fibonacci, los 2 primeros términos son 0 y 1, y a partir 
del segundo cada uno se calcula sumando los dos anteriores términos de la serie.

[0, 1, 1, 2, 3, 5, 8, ...]

"""

count = 2
fibonacci=[0, 1]
while count <= 59:
    longitud = len(fibonacci)-1
    nuevo=(fibonacci[longitud-1] + fibonacci[longitud])
    fibonacci.append(nuevo)
    count+=1
print(fibonacci)


"""Guardar en `factorial` el factorial de 30
El factorial (símbolo:!) Significa multiplicar todos los números enteros desde
el 1 hasta el número elegido.

Por ejemplo, el factorial de 5 se calcula así:

5! = 5 × 4 × 3 × 2 × 1 = 120
"""
factorial=1
for i in range(1,31):
  factorial=factorial*i




"""Guarde en lista `pares` los elementos de la siguiente lista que esten 
presentes en posiciones pares, pero solo hasta la posición 80.
"""

lista3 = [941, 149, 672, 208, 99, 562, 749, 947, 251, 750, 889, 596, 836, 742, 512, 19, 674, 142, 272, 773, 859, 598, 898, 930, 119, 107, 798, 447, 348, 402, 33, 678, 460, 144, 168, 290, 929, 254, 233, 563, 48, 249, 890, 871, 484, 265, 831, 694, 366, 499, 271, 123, 870, 986, 449, 894, 347, 346, 519, 969, 242, 57, 985, 250, 490, 93, 999, 373, 355, 466, 416, 937, 214, 707, 834, 126, 698, 268, 217, 406, 334, 285, 429, 130, 393, 396, 936, 572, 688, 765, 404, 970, 159, 98, 545, 412, 629, 361, 70, 602]

pares=list()
for i in range(0,81,2):
  pares.append(lista3[i])




"""Guarde en lista `cubos` el cubo (potencia elevada a la 3) de los números del 
1 al 100. 
"""
cubos=list()
for i in range(1,101):
  cubos.append(i**3)
  #print(cubos[i])





"""Encuentre la suma de la serie 2 +22 + 222 + 2222 + .. hasta sumar 10 términos 
y guardar resultado en variable `suma_2s` 
"""
suma_2s=0
suma=1
l=list()
for i in range(1,11):
    suma='2'*i
    suma=int(suma)
    l.append(suma)

for el in l:
    suma_2s=el+suma_2s



"""Guardar en un string llamado `patron` el siguiente patrón llegando a una 
cantidad máxima de asteriscos de 30. 
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
"""

patron = ''
for numero in range (1,31):
    patron += "*"*(numero) + "\n"
for numero in range (29,0, -1):
    if numero == 1:
        patron += "*"*(numero)    
    else:
        patron += "*"*(numero) + "\n"
print (patron)

# patron = ''
# for numero in range (1,31):
#     patron += "*"*(numero) + "\n"
# for numero in range (29,0, -1):
#     patron += "*"*(numero) + "\n"
# patron=patron.strip()
#print(patron)

#repr(patron)




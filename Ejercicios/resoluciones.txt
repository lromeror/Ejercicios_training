"""
Escriba un programa en el que el usuario ingrese una cantidad de segundos y se le impriman en pantalla la
cantidad de horas, minutos y segundos.
"""
#user = input ("Ingrese una cantidad de segundos: ")
#user = int(user)
#horas = user//3600
#sobrante = user%3600
#minutos = (sobrante)//60
#segundos = (sobrante)%60
#print(f"{user} segundos representan {horas} horas {minutos} minutos {segundos} segundos")
"""
Cree un programa que simule un juego de Adivinanza, en este caso el jugador debe adivinar la palabra
“Profesor”, mostrando solamente “P______r”. Se debe mostrar la pista: “se dedica profesionalmente a la
enseñanza”. Si el jugador adivina la palabra, el programa debe imprimir True, caso contario False.
"""
#import random as rd
#print("Adivina la palabra")
## se puede poner más intento en este caso lo limito a uno
## Imagino que solo supiera primer parcial
#l_palabras = ['Profesor','Cantante','Futbolista','Presidente']
#pistas = ['se dedica profesionalmente a la enseñanza','se dedica profesionalmente a cantar','se dedica profesionalmente a jugar futbol','se dedica a gobernar un pais']
#palabra = rd.sample (l_palabras,1) [0]
#pista = pistas[ l_palabras.index(palabra) ]
#print(f"Pista :{pista}")
#mostrar = palabra[0] + ( "_"*(len(palabra)-2) ) + palabra[-1]
#print(mostrar)
#user = input("Ingrese la palabra: ").strip()
#if user == palabra : 
#    print (True)
#else:
#    print (False)
"""
Escriba un programa que permita ver a los estudiantes de la ESPOL si reprobaron una materia o no (en
una materia donde la ponderación es 80% teorico y 20% práctico). El programa pedirá al usuario ingresar
su nota de primer parcial, su nota de segundo parcial, su nota de mejoramiento y su nota práctica,
todas sobre 100 (como se muestra en el sistema académico). Además, pedirá ingresar su numero de faltas
y su número total de clases. Recodemos que aquel estudiante que tenga menos de 60/100 de promedio
académico o menos 60% de asistencia a clases están quedado.
"""
#print("Importante : Ingrese sus notas sobre 100. ")
#parcial1 = float(input("Ingrese nota primer parcial: "))
#parcial2= float(input("Ingrese nota segundo parcial: "))
#recuperacion = float(input("Ingrese nota mejoramiento: "))
#pratica = float(input("Ingrese nota practica: "))
#faltas = int(input("Ingrese numero de faltas: "))
#clases = int(input("Ingrese numero total de clases: "))
#ponderacion_teo = 0.8
#ponderacion_prac = 0.2
#lista_notas = [parcial1,parcial2,recuperacion]
#lista_notas.sort(reverse=True) 
#nota1 = lista_notas[0]
#nota2 = lista_notas[1]
#teorico_pro = ((nota1+nota2)/2) * ponderacion_teo
#practico_pro = pratica * ponderacion_prac
#promedio_final  = teorico_pro + practico_pro
#asistencia = (clases-faltas)/clases
#print(nota1,nota2,promedio_final,practico_pro,teorico_pro)
#if promedio_final < 60 or asistencia < 0.6:
#    print ("Has reprobado la materia")
#else : 
#    print("Has aprobado la materia")

"""
La siguiente es una lista de personas que participan en un sorteo de electrodomésticos:
[“Luis”,”Rafael”,”Diego”,”Carlos”,”Rodrigo”,”Steven”,”Jose”,”Miguel”,”Luka”,”Jorge”,”Mike”,”Ibai”]
Usando funciones de listas, escriba un programa en el que se saque tres ganadores de forma aleatoria y
muestre el premio que consigue cada ganador. El primer ganador obtiene una Licuadora, el segundo
ganador obtiene una Freidora de Aire y el tercer ganador obtiene una Refrigeradora. Los ganadores se
pueden repetir.
"""
#import random as rd
#lista = ["Luis","Rafael","Diego","Carlos","Rodrigo","Steven","Jose","Miguel","Luka","Jorge","Mike","Ibai"]
#for x in range(3) :
#    num = rd.randint(0,len(lista)-1)
#    if x == 0 :
#        print (f"El ganador de la licuadora es {lista[num]}")
#    elif x == 1 : 
#        print (f"El ganador de la Freidora de Aire es {lista[num]}")
#    else :
#        print (f"El ganador de la Refrigeradora es {lista[num]}")

"""
Una avioneta está a punto de quedarse sin gasolina, entonces los pasajeros se sortean los únicos tres
paracaídas que quedan. A continuación, se encuentra la lista de pasajeros que están volando en esa
avioneta:
[“Luis”,”Rafael”,”Diego”,”Carlos”,”Rodrigo”,”Steven”,”Jose”,”Miguel”,”Luka”,”Jorge”,”Mike”,”Ibai”]
Usando funciones de listas, escriba un programa en el que realice los sorteos imprimiendo los ganadores
(uno por vez), recuerde que el que gana el paracaídas, ya no participa en el siguiente sorteo. Finalmente
muestre la lista de las personas que se quedaron en la avioneta.
"""
#import random as rd
#lista = ["Luis","Rafael","Diego","Carlos","Rodrigo","Steven","Jose","Miguel","Luka","Jorge","Mike","Ibai"]
#ganadores = rd.sample(lista,3)
#print ("Ganadores: ")
#quedados = lista
#for ganador in ganadores :
#    print (ganador)
#    quedados.remove(ganador)
#print (f"Los que quedaron en la avioneta son:  {quedados}")
"""
Implemente la función buscar_par_descendente(l_numeros) que recibe una lista de números enteros.
La función debe encontrar el primer par de elementos adyacentes en la lista l_numeros que están en
orden descendente y devuelve el índice del primer elemento del par. Si no existe tal par, devuelve
None.
Ejemplo:
Para la lista [1,3,4,6,4,7,6] el retorno sería tres
Para la lista [1,3,4,5,6,7,6] el retorno sería 5
Para la lista [1,3,4,5,6,7,8] el retorno sería None
Luego escriba un programa principal que genere una lista de 17 números aleatorios entre 15 y 28 y
muestre el resultado de invocar a su función con esa lista.
"""
#import random as rd
#def buscar_par_descendente(l_numeros):
#    for i in range(len(l_numeros)-1):
#        if l_numeros[i] > l_numeros[i+1]:
#            return i
#lista=[]
#for n in range(17):
#    num = rd.randint(15,28)
#    lista.append(num)
#print(buscar_par_descendente(lista))
"""
Implemente la función justificar(linea, tamaño) que recibe una línea de texto y un entero.
Suponga que la línea está compuesta por dos o más palabras separadas por un espacio en blanco y que
su longitud es menor a tamaño. En la línea no hay dígitos ni símbolos especiales (solo letras y espacios
en blanco). Entonces su función debe completar la longitud de la línea hasta llegar a ser exactamente
igual a tamaño. Para esto agregue lo más equitativamente posible espacios en blanco entre las
palabras de la línea empezando desde la izquierda. Observe que la nueva línea no puede empezar ni
terminar con espacios en blanco.
La función debe retornar esa nueva línea.
Ejemplo:
Si se pide justificar a tamaño de 61 la frase:
"Este es un buen día para aprobar fundamentos"
La función retornaría:
"Este--- es--- un--- buen-- día-- para-- aprobar-- fundamentos"
Observe que se usa "-" para representar los espacios en blanco añadidos. En la solucion final no se debe
usar "-" sino espacios en blanco.
"""
#def justificar(linea, tamaño):
#    resultado = tamaño - len(linea)
#    n_espacios= linea.count(' ')
#    cant_exac = resultado // n_espacios
#    sobrantes= resultado % n_espacios
#    lista= linea.split(" ")
#    for i in range(sobrantes):
#        lista[i] += " "
#    unir = " "*(cant_exac+1)
#    linea_justificada = unir.join(lista)
#    return linea_justificada
#
#result = justificar("Este es un buen día para aprobar fundamentos.",100)
#print (result)

"""
Implementa la función calcular_porcentajes(l_partidos,l_goles) que recibe dos listas paralelas.
La lista l_partidos es una lista de strings con los nombres de los equipos que se enfrentan en cada
partido de la primera etapa del mundial de Qatar. La lista l_goles es también una lista de strings con
los goles marcados por cada uno de los equipos en los partidos representados en la lista l_partidos.
Ejemplo:
l_partidos = ["CAT-ECU","ARG-MEX","BRA-SUI","ECU-SEN",...]
l_goles = ["0-2","2-0","1-0","2-1",...]
Debe retornar una nueva lista de tuplas con los puntos en esta fase del mundial. Recuerde que una
victoria otorga tres puntos al equipo ganador. Un empate otorga 1 punto a ambos equipos y, la derrota
0 puntos al equipo perdedor.
Ejemplo del retorno:
[("ECU",7),("CAT",0),("BRA",9),("ARG",5),...]
"""
#l_goles = ["0-2","1-1","4-1","2-0"]
#l_partidos = ["CAT-ECU","ARG-MEX","BRA-SUI","ECU-SEN"]
#def calcular_puntajes(l_partidos,l_goles) :
#    paises=[] 
#
#    puntos=[] 
#    for partido,resultado in zip(l_partidos,l_goles) : 
#        pais1,pais2 = partido.split("-") 
#        if pais1 not in paises:
#            paises.append(pais1)
#        if pais2 not in paises:
#            paises.append(pais2)
#        pos1 = paises.index(pais1)  
#        pos2 = paises.index(pais2)  
#        if pos1 > len(puntos)-1 :   
#            puntos.append(0)
#        if pos2 > len(puntos)-1 : 
#            puntos.append(0)
#        
#        gm1,gm2 = resultado.split("-")
#        gm1 = int(gm1) 
#        gm2 = int(gm2)  
#        if gm1 > gm2 :      
#            puntos[pos1] += 3    
#        elif gm2 > gm1 :     
#            puntos[pos2] += 3
#        elif gm1 == gm2 :    
#            puntos[pos1] += 1
#            puntos[pos2] += 1
#    listaf = []
#    for pais,puntos_p in zip(paises,puntos) :
#        tupla = (pais,puntos_p)
#        listaf.append(tupla)
#    return listaf
#
#listaf = calcular_puntajes(l_partidos,l_goles)
#print(listaf)
"""
Escriba un programa que imprima todos los números del 1 al 100.
"""
#[print(x) for x in range(1,101)]
"""
Escriba un programa que imprima todos los números pares del 1 al 100.
"""
#for x in range(1,101):
#    if (x%2) == 0 :
#        print(x)
"""
Escriba un programa que imprima todos los números impares del 1 al 100.
"""
#for x in range(1,101):
#    if (x%2) != 0 :
#        print(x)
"""
Escriba un programa que imprima todos los números que existen entre dos numeros dados por el usuario.
"""
#num1 = int( input("Ingrese un numero inicial : ") )
#num2 = int( input("Ingrese un numero final: ") )
#if num1 < num2 :
#    [print(x) for x in range(num1+1,num2)]
#else :
#    [print(x) for x in range(num1-1,num2,-1)]
"""
#Escriba un programa que imprima todos los números pares que existes entre dos numeros dados por el usuario.
#"""
#num1 = int( input("Ingrese un numero inicial : ") )
#num2 = int( input("Ingrese un numero final: ") )
#if num1 < num2 :
#    for x in range(num1+1,num2):
#        if (x%2) == 0 :
#            print(x)
#else :
#    for x in range(num1-1,num2,-1):
#        if (x%2) == 0 :
#            print(x)
""" 
Escriba un programa que lea un número de n cifras impares y determine si es igual al revés del número.
"""
#num1 = input ("Ingrese un numero de n cifras impares: ") 
#num2 = num1[::-1]
#print(num2)
#if num1 == num2 :
#    print("Es igual al revés del número")
#else: 
#    print("No es igual al revés del número")
""" 
Escriba una función que reciba una palabra y verifique si es palíndroma o no es palíndroma(Al revés se escriba igual).
"""
#def es_Palindroma(palabra) :
#    al_reves = palabra[::-1]
#    if palabra == al_reves :
#        print("Es palíndroma")
#    else: 
#        print("No es palíndroma")
#
#es_Palindroma("reconocer")
"""
La nota práctica de fundamentos de programación es el promedio de todos los talleres; sin
embargo, decide eliminar la nota de taller más baja y promediar el resto. Escriba un programa que
le pregunte al estudiante cuantos talleres ha dado, le pida ingresar las de los mismos, y le muestre
cuál fue su taller más bajo y cuál es su promedio con esa medida.
"""
#n_talleres = int( input("Ingrese el número de talleres: ") )
#notas_todas = []
#for x in range(n_talleres):
#    nota = float( input(f"Ingrese la nota del taller {x+1}: ") )
#    notas_todas.append(nota)
#notas = notas_todas.copy()
#notas.sort(reverse=True)
#bajo = notas.pop()
#promedio = sum(notas)/len(notas)
#pos = notas_todas.index(bajo)
#print(f"La nota más baja es el taller {pos+1} con {bajo}  y el promedio final es {promedio}")
"""
Escriba tres funciones que imprima un mensaje de saludo:
1. Que no reciba parámetros y no retorne nada.
2. Que reciba como parámetro un nombre y lo incluya en el saludo.
3. Que pueda recibir un nombre parámetro o no, en caso de que lo reciba inclúyalo en el saludo,
caso contrario que el saludo sea genérico, y que retorne el saludo.
"""
#def funcion1 () : 
#    print ("Hola")
#
#def funcion2 (nombre) :
#    print (f"Hola {nombre}")
#
#def funcion3 (nombre = None):
#    if nombre == None:
#        print ("Hola ")
#    else : 
#        print (f"Hola {nombre}")
##Ejemplo
#funcion1()
#funcion2("Taws")
#funcion3()
#funcion3("Swat")
"""
Implemente una función, que nos devuelva el volumen de una esfera. Devuelva -1 si el radio es
menor o igual a 0.
"""
#import math
#def volumen_Esfera (radio):
#    if radio < 0 : 
#        return -1
#    else :
#        return (4/3) * (math.pi) * (radio**3)
##Ejemplo
#print(volumen_Esfera(2))
#print(volumen_Esfera(-1))

"""
Implemente una función, que reciba una lista cualquiera de enteros, y devuelva otra lista sin
elementos repetidos.
"""
#def eliminar_Repetidos (lista):
#    lista2 = []
#    for x in lista :
#        if x not in lista2 :
#            lista2.append(x)
#    return lista2
#
##Aplicando conjuntos, pero aqui pierden el orden 
#def eliminar_Repetidos_2 (lista):
#    return list(set(lista))
#
#print( eliminar_Repetidos([2,3,4,2,1]) ) 
#print( eliminar_Repetidos_2([2,3,4,2,1]) )
"""
Implemente una función, que reciba una lista con nombres completos de personas(2 nombres y 2 apellidos ) y un string con el
nombre a buscar. Usando las funciones de string, devuelva una lista, que contenga los nombres completos de las personas donde el nombra a buscar coincida con los nombres de la persona, 
Nota: al momento de verificar si son iguales no tome en cuenta si las Mayúsculas y Minúsculas.
def buscar(arreglo, nombreABuscar).
"""
#def buscar (arreglo, nombreABuscar) : 
#    lista = []
#    for nombre_c in arreglo :
#        nombre_c = nombre_c.strip().lower()
#        if nombreABuscar.lower() in nombre_c.split(" ") :
#            lista.append(nombre_c.title())
#    return lista
#
##Ejemplo
#lista = ["Pepito Juanito Mercado Diaz",
#        "Lionel Andrés Messi Cuccittini",
#        "Cristiano Ronaldo Dos Santos Aveiro",
#        "Neymar da_Silva Santos Júnior",
#        "Kylian Mbappé Lottin",
#        "Lionel Kylian Caicedo Perez",
#        "Neymar Cristiano Paez Diaz"]
#print(buscar (lista, "Neymar"))
"""
Implemente una que reciba un numero entero positivo y determine el factorial de ese número.
"""
#def factorial (num) : 
#    if num == 0 : 
#        return 1
#    else :
#        return num * factorial(num-1)
#print(factorial(4))

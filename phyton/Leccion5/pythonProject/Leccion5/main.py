# Comenzamos con funciones
# mi_funcion() # No se puede llamar antes de definir una funcion
# Definimos una funcion
from pickle import PROTO


def mi_funcion(): # Para identificar a la funcion utilizamos parentesis
    print("Saludos a todos los alumnos de la Tecnicatura")

mi_funcion() # Estamos llamando a la funcion
mi_funcion() # Se puede llamar a una funcion N cantidad de veces

#Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+" "+lastName)
person = ["Gonzalo", "Bucca"]
show(person[0], person[1]) #Pasamos uno por uno los datos de la lista a la funcion
show(*person) #Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Ramiro", "Vidal") #Desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Santos", "name": "Matias"}
show(**person3)

#Repaso for else
numers = [1, 2, 3, 4, 5] #Aun con la lista vacia se va a ejecutar el else
for n in numers:
    print(n)
    if n == 3:
        break #Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termino")

#List comprehension, lista de comprension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] #Esto regresa una nueva lista
print(alongP)

bottleC = [{"name":"Quilmes", "country": "Arg"},
           {"name":"Corona", "country": "Mx"},
           {"name":"Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b ["country"] == "Arg"]
print(Arg)
print(bottleC)

#Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que nos ven a traves del canal de YouTube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Jorge", "Lucero")
mi_funcion2("Gonzalo", "Bucca")
mi_funcion2("Juan Carlos", "Bucca")

#La palabra return en funciones
#Creamos una funcion para sumar
def sumar(a, b):
    return a + b
#resultado = sumar(78, 22)
#print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55, 45)}")

def sumar2(a = 0, b = 0): #Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22 , 66)}")

#Argumentos, variables en funciones
def listarNombres(*nombres): #Normalmentre se utiliza: *args
    for nombre in nombres: #Se va a convertir en una tupla
        print(nombre)
listarNombres("Lucas", "Jose", "Claudia", "Rosa", "Maria")
listarNombres("Marcos", "Daniel", "Romina", "Pepe", "Marcela", "Carlos")

def listarTerminos(**terminos): #Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): #Kwargs significa: key word argument
        print(f"{llave} : {valor}")

listarTerminos() #No recibe nada, nada se va a mostrar
listarTerminos(IDE="Integrated Develoment Enviroment", PK="Primary Key")
listarTerminos(Nombre="Lionel Messi")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ["Tito", "Pedro", "Carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")
#desplegarNombres(10, 11) #No es un objeto iterable
desplegarNombres((10, 11)) #La convertimos a una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22, 55]) #La convertimos en una lista

#Funciones recursivas
def facrotial(numero):
    if numero == 1:
        return 1
    else:
        return numero *facrotial(numero-1) #Caso recursivo
numeroFactorial = int(input("Digite el numero para calcular el factorial: "))
resultado = facrotial(5) #Lo hacemos en codigo duro
print(f"El factorial del numero 5 es: {resultado}")

#Tarea que el usuario ingrese el numero para calcular el factorial
numeroFactorial = int(input("Digite el numero para calcular el factorial: "))
resultado = facrotial(numeroFactorial)
print(f"El factorial del numero {numeroFactorial} es: {resultado}")
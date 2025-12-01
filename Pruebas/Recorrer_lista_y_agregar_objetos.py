#importamos de "Persona.py" a la CLASE personaObjeto
from Persona import personaObjeto

#Creamos una nueva instancia del objeto personaObjeto
nuevaPersona = personaObjeto()
#Creamos una lista para rellenar luego
listaObjeto = []

i = 0

i= input("Cuantas pesonas son: ")

x = 0
# Iteramos para agregar la cantidad de personas que sean solicitadas
for x in range(int(i)):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    altura = float(input("Altura: "))
   # Le damos valores a la instancia del objeto
    nuevaPersona.nombre = nombre
    nuevaPersona.apellido = apellido
    nuevaPersona.edad = edad
    nuevaPersona.altura = altura

    #Agregamos a la lista la instancia
    listaObjeto.append(nuevaPersona)
    # NOTA: append es una FUNCION asi que se utiliza parentecis
    x += 1
    
d = 0    

busqueda = input("Nombre para buscar: ")

# Recorremos la lista para buscar a la persona que nos solicitan.
for z in listaObjeto:
    if z.nombre.lower() == busqueda.lower():
        persona_encontrada = z        
        break

#Si la persona se encontro la mostramos en pantalla, sino damos un mensaje de error

if persona_encontrada:
    print("---------------------------------")
    print(f"Nombre:   {persona_encontrada.nombre} {persona_encontrada.apellido}")
    print(f"Edad:     {persona_encontrada.edad} años")
    print(f"Altura:   {persona_encontrada.altura} metros")
    print("---------------------------------")
else:
    print("No se encontro a la personaObjeto")

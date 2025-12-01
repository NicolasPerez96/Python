class campeon:
    #Creamos la clase campeon y le damos atributos
    def __init__ (self, nombre, fuerza, agilidad, velocidad, inteligencia):
        self.nombre = nombre
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.velocidad = velocidad
        self.inteligencia = inteligencia
        self.vida = 100
        
class guerrero:
    def __init__(self, nombre):
    
        super().__init__(
            nombre = nombre,
            fuerza = 15,
            agilidad = 7,
            velocidad = 10,
            inteligencia = 5                                  
        )
        self.vida = 200

class mago:
    def __init__(self, nombre):
        
        super().__init__(
            nombre = nombre,
            fuerza = 7,
            agilidad = 10,
            velocidad = 10,
            inteligencia = 20
        )
        self.mana = 200
        
class picaro:
    def __init__(self, nombre):
        
        super().__init__(
            nombre = nombre,
            fuerza = 10,
            agilidad = 20,
            velocidad = 16,
            inteligencia = 12
        )
        self.probCritica = 1.5
        

        

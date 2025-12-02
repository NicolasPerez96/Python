class campeon:
    #Creamos la clase campeon y le damos atributos
    def __init__ (self, nombre, fuerza, agilidad, velocidad, inteligencia):
        self.nombre = nombre
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.velocidad = velocidad
        self.inteligencia = inteligencia
        self.vida = 120
        self.vida_actual = self.vida
        self.vida_restante = self.vida_actual
        
    def recibirDaño (self, dañoRecibido):
        self.vida_actual -= dañoRecibido
        self.vida_restante = self.vida_actual
        print(f"{self.nombre} recibio {dañoRecibido} le queda {self.vida_restante} de vida.")
        return self.vida_actual
    
    def atacar(self):
        daño = self.fuerza * (self.agilidad * 0.5)
        return daño
    
    def estaVivo(self):          
        return self.vida_actual > 0
    
    def recuperarVida(self, recuperar):
        self.vida_actual += recuperar

        if self.vida_actual > self.vida:
            self.vida_actual = self.vida

        print(f"{self.nombre} recuperó {recuperar} de vida.")
        return self.vida_actual 
        
class guerrero(campeon):
    def __init__(self, nombre):
    
        super().__init__(
            nombre = nombre,
            fuerza = 15,
            agilidad = 7,
            velocidad = 10,
            inteligencia = 5                                  
        )
        self.vida = 200
        self.vida_actual = self.vida
        self.daño = 30
        self.daño_actual = self.daño
    
        

class mago(campeon):
    def __init__(self, nombre):
        
        super().__init__(
            nombre = nombre,
            fuerza = 7,
            agilidad = 10,
            velocidad = 10,
            inteligencia = 20
        )
        #self.mana = 200
        
    #def lanzarMagia(self, dañoMagico):
    #    dañoMagico = self.inteligencia
    #    return dañoMagico
        
class picaro(campeon):
    def __init__(self, nombre):
        
        super().__init__(
            nombre = nombre,
            fuerza = 10,
            agilidad = 20,
            velocidad = 16,
            inteligencia = 12
        )
       # self.probCritica = 1.5
    
        

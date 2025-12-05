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
        
        self.experiencia = 0
        self.experiencia_subir_nivel = 100
        self.nivel = 1
        
        self.mana = 100
        self.mana_actual = self.mana
        
    
            
        
        
    def recibirDaño (self, dañoRecibido):
        self.vida_actual -= dañoRecibido
        print(f"{self.nombre} recibio {dañoRecibido} le queda {self.vida_actual} de vida.")
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
    
    def subirNivel(self):
        print (f"{self.nombre} ha subido de nivel!")
        self.experiencia_subir_nivel = self.experiencia + (self.experiencia * 0.50)
        if isinstance(self, guerrero):
            print(f"""Tus estadisticas han subido!
                  Vida +50
                  Mana +20
                  Fuerza +4
                  Agiliadd +2
                  Velocidad +2
                  Inteligencia +1""")
            self.fuerza += 4
            self.agilidad += 2
            self.velocidad += 2
            self.inteligencia += 1
            self.vida += 50
            self.vida_actual += 50
            self.mana += 20
            self.mana_actual = self.mana
        elif isinstance(self, mago):
            print(f"""Tus estadisticas han subido!
                  Vida +20
                  Mana +75
                  Fuerza +1
                  Agiliadd +2
                  Velocidad +3
                  Inteligencia +4""")
            self.fuerza += 1
            self.agilidad += 2
            self.velocidad += 3
            self.inteligencia += 4
            self.vida_actual += 20
            self.vida += 20
            self.mana_actual += 75
            self.mana_actual = self.mana
        elif isinstance(self, picaro):
            print(f"""Tus estadisticas han subido!
                  Vida +35
                  Mana +25
                  Fuerza +2
                  Agiliadd +4
                  Velocidad +5
                  Inteligencia +2""")
            self.fuerza += 2
            self.agilidad += 4
            self.velocidad += 5
            self.inteligencia += 2
            self.vida_actual += 35
            self.vida += 35
            self.mana_actual += 25
            self.mana_actual = self.mana
        
        
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
    
   

class enemigoGenerico:
    def __init__(self, nombre, daño, defensa, vida):
        self.nombre = nombre
        self.daño = daño
        self.defensa = defensa
        self.vida = vida
        self.vida_actual = self.vida
        self.vida_restante = self.vida_actual
        
    def recibirDaño (self, dañoRecibido):
        self.vida_actual -= (dañoRecibido - self.defensa)
        return print(f"{self.nombre} recibio {dañoRecibido} le queda {self.vida_actual} de vida.") 
    
    def atacar(self):
        return self.daño   

class goblin(enemigoGenerico):
    def __init__(self):        
        
        super().__init__(
            nombre = "Goblin" 
            daño = 15,
            defensa = 5,
            vida = 50            
        )
         
        
        
class lobo(enemigoGenerico):
    def __init__(self):
        
        super().__init__(
            nombre = "Lobo"
            daño = 25,
            defensa = 8,
            vida = 75
        )

class troll(enemigoGenerico):
    def __init__(self):
        
        super().__init__(
            nombre = "Troll"
            daño = 40,
            defensa = 15,
            vida = 150
        )     
        
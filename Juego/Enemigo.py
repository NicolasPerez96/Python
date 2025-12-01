class enemigoGenerico:
    def __init__(self, daño, defensa, vida):
        self.daño = daño
        self.defensa = defensa
        self.vida = vida
    

class goblin:
    def __init__(self):        
        
        super().__init__(
            daño = 15,
            defensa = 5,
            vida = 50
        )    
        
        
        
class lobo:
    def __init__(self):
        
        super().__init__(
            daño = 25,
            defensa = 8,
            vida = 75
        )
        

class troll:
    def __init__(self):
        
        super().__init__(
            daño = 40,
            defensa = 15,
            vida = 150
        )
        
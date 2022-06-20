class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        perimetro = self.a + self.b +  self.c
        return perimetro
    
    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif self.a == self.b != self.c or self.a != self.b == self.c or self.a == self.c != self.b: 
            return 'isósceles'
        else:
            return 'escaleno'
# Crear una clase Rectangulo, con atributos base y altura.
# Crear tambien el constructor de la clase y los metodos necesarios para calcular el area y el perımetro.

class Rectangulo:

    base = 0
    altura = 0

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perımetro(self, base, altura):
        return print(base* altura)

# instancia

rec = Rectangulo(50,2)

rec.perımetro(5,2)
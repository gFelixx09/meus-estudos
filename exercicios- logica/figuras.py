class figura:
  def __init__(self, nome):
    self.nome=nome

class retangulo(figura):
      def __init__(self,nome, base, altura):
        super().__init__(nome)
        self.base=base
        self.altura=altura

      def area(self):
        return self.base * self.altura
      
      def perimetro(self):
        return 2 * (self.base + self.altura)
      
class triangulo(figura):
        def __init__(self,nome, base, altura, l1, l2, l3):
          super().__init__(nome)
          self.base= base
          self.altura = altura
          self.l1=l1
          self.l2=l2
          self.l3=l3

        def area(self):
          return (self.base * self.altura) / 2
      
        def perimetro(self):
          return self.l1 + self.l2 + self.l3
     
class circulo(figura):
        def __init__(self,nome, raio ):
          super().__init__(nome)
          self.raio=raio
      
        def area(self):
          return 3.14 * (self.raio ** 2)
      
        def perimetro(self):
          return 2*self.raio*3.14
      
nome = input("Qual o nome do produto: ").lower()

if nome == "retangulo":
  base = float(input("Qual a base: "))
  altura = float(input("Qual a altura: "))
  r = retangulo("retangulo", base, altura)
  resposta = r.area()
  resp = r.perimetro()

  print("A area do {} é {}, e o perimetro {}".format(nome,r.area(), r.perimetro()))
          
elif nome == "triangulo":
  base = float(input("Qual a base: "))
  altura=float(input("Qual a altura: "))
  l1=float(input("Qual o lado 1: "))
  l2=float(input("Qual o lado 2: "))
  l3=float(input("Qual a lado 3: "))
  t = triangulo("triangulo", base, altura, l1, l2, l3)
  resposta = t.area()
  resp = t.perimetro()

  print("A area do triangulo é {}, e o perimetro é {}".format(t.area(), t.perimetro()))

elif nome == "circulo":
  raio = float(input("Qual o raio do circulo: "))
  c =circulo("circulo", raio)
  resposta = c.area()
  resp = c.perimetro()
           
  print(f'A area do {nome} é {c.area()}, e o perimetro é {c.perimetro()}')

else:
  print("figura geometrica invalida")
           

           
      
      


    
    
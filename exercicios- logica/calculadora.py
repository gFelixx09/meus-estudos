class calculadora:
  def __init__(self):
    pass
  
  def soma(self, n1, n2):
    return n1 + n2
  
  def sub(self, n1, n2):
    return n1 - n2
  
  def mult(self, n1, n2):
    return n1 * n2
  
  def div(self, n1, n2):
    if n2==0:
      return "Operação invalida"
      
    return n1 / n2


  def calcular(self):
    n1=float(input("Qual o número: "))
    n2=float(input("Qual o número: "))
    op=input("Qual operação você quer fazer: ")

    if op == "+":
      resultado =self.soma(n1,n2)
    elif op == "-":
      resultado=self.sub(n1,n2)
    elif op == "*":
      resultado=self.mult(n1,n2)
    elif op == "/":
      resultado=self.div(n1,n2)
    else:
      resultado="operação invalida"

    print("O resultado é {}".format(resultado))

calc=calculadora()
calc.calcular()
     
  
  
      

    
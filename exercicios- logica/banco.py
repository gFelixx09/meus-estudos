class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def calcular_bonus(self):
        print(f"O funcionário comum {self.nome} não possui bônus específico cadastrado.")
        return 0

class Gerente(Funcionario):
    def calcular_bonus(self):
        bonus = self.salario * 0.15
        print(f"O Gerente {self.nome} recebeu um bônus de R${bonus:.2f}")
        return bonus

class Vendedor(Funcionario):
    def calcular_bonus(self):
        bonus = self.salario * 0.10
        print(f"O Vendedor {self.nome} recebeu um bônus de R${bonus:.2f}")
        return bonus


nome = input("Digite o nome do funcionário: ")
cargo = input("Digite o cargo do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

if cargo.lower() == "gerente":
    funcionario_atual = Gerente(nome, cargo, salario)
elif cargo.lower() == "vendedor":
    funcionario_atual = Vendedor(nome, cargo, salario)
else:
    funcionario_atual = Funcionario(nome, cargo, salario)


funcionario_atual.calcular_bonus()
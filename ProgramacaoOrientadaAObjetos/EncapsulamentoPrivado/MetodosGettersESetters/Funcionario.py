class Funcionario:
    def __init__(self, nome: str, cargo: str, salario: float) -> None:
        self.__nome = nome
        self.__cargo = cargo
        self.salario = salario  # Utilize o setter para validar o salário

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def cargo(self) -> str:
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: str) -> None:
        self.__cargo = cargo

    @property
    def salario(self) -> float:
        return self.__salario

    @salario.setter
    def salario(self, salario: float) -> None:
        self.__validarSalario(salario)

    def __validarSalario(self, salario: float) -> None:
        if salario <= 0:
            raise ValueError('Erro! Salário não pode ser inferior ou igual a zero!')
        else:
            self.__salario = salario

    def __calcularAumento(self, porcentagem: float) -> float:
        if porcentagem < 0:
            raise ValueError('Erro! A porcentagem de aumento não pode ser negativa!')
        aumento = (porcentagem / 100) * self.__salario
        return self.__salario + aumento

    def aumentarSalario(self, porcentagem: float) -> None:
        self.__salario = self.__calcularAumento(porcentagem)

# Teste da classe Funcionario
funcionario1 = Funcionario('Desenvolvedor Arthur Yokomizo', 'Desenvolvedor Python', 25000)
print(funcionario1.salario)  # 25000

funcionario1.salario = 30000
print(funcionario1.salario)  # 30000

funcionario1.aumentarSalario(10)
print(funcionario1.salario)  # 33000

try:
    funcionario1.salario = -1000
except ValueError as e:
    print(e)  # Erro! Salário não pode ser inferior ou igual a zero!

try:
    funcionario1.aumentarSalario(-5)
except ValueError as e:
    print(e)  # Erro! A porcentagem de aumento não pode ser negativa!

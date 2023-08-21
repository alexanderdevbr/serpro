# Classe de pessoas (nivel mais elevado de abstracao)
class Pessoa:
    def __init__(self, nome, cpf: str):
        self._nome = nome
        self._cpf = cpf

# Classe de fucionario padrão
class Funcionario(Pessoa):
    def __init__(self, nome, cpf: str, salario: float):
        super().__init__(nome, cpf)
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10

# Classe de funcionario tipo Gerente
class Gerente(Funcionario):
    def __init__(self, nome, cpf: str, salario: float, senha: str, qtd_gerenciados: int):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados

    def autentica(self, senha):
        if self._senha == senha:
            print(f"{self._nome} Autenticado!")
            return True
        else:
            print("Acesso Negado!")
            return False
    
    def get_bonificacao(self):
        return super().get_bonificacao() + 1000

# Classe de controle bonificacao
class ControleBonificacao:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes
        self._lista = []

    def registra(self, funcionario: Funcionario):
        if(hasattr(funcionario, 'get_bonificacao')):
            self._total_bonificacoes += funcionario.get_bonificacao()
            self._lista.append(funcionario)
        else:
            print('instância {} não implementa get_bonificacao()'.format(funcionario.__class__.__name__))
    
    def totalBonificacao(self):
        print(f"Total de bonificação: {self._total_bonificacoes}")
    
    def totalBonificacaoLista(self):
        totalBonificacao = 0
        for funcionario in self._lista:
            totalBonificacao += funcionario.get_bonificacao()
        print(f"Total bonificacao Lista com {len(self._lista)} elementos: {totalBonificacao}")

# Cliente
class Cliente(Pessoa):
    def __init__(self, nome, cpf: str, desconto: float) -> None:
        super().__init__(nome, cpf)
        self._desconto = desconto

# Principal
if(__name__ == '__main__'):
    p1 = Funcionario("Maria", "123.123.123-00", 1250.00)
    p2 = Gerente("Joao", "456.456.456-00", 2100.00, "teste123", 15)
    p3 = Cliente("Helena", "789.789.789-88", 10.75)

    print(vars(p1))
    print(vars(p2))
    print(vars(p3))
    print(f"Bonificação: {p1.get_bonificacao()}")
    print(f"Bonificação: {p2.get_bonificacao()}")

    cb = ControleBonificacao()
    cb.registra(p1)
    cb.registra(p2)
    cb.registra(p3)
    cb.totalBonificacao()
    cb.totalBonificacaoLista()
    print(vars(cb))
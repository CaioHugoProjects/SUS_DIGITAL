class Profissional:

    def __init__(self, nome: str, cpf: str, especialidade: str, registro: str, unidade: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__especialidade = especialidade
        self.__registro = registro  
        self.__unidade = unidade
        self.__agenda = []  

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome: str):
        if len(novo_nome) < 3:
            raise ValueError("Nome do profissional deve ter ao menos 3 caracteres.")
        self.__nome = novo_nome

    def get_cpf(self):
        return self.__cpf

    def get_especialidade(self):
        return self.__especialidade

    def set_especialidade(self, nova_especialidade: str):
        self.__especialidade = nova_especialidade

    def get_registro(self):
        return self.__registro

    def get_unidade(self):
        return self.__unidade

    def set_unidade(self, nova_unidade: str):
        self.__unidade = nova_unidade

    def adicionar_agendamento(self, agendamento):
        
        self.__agenda.append(agendamento)

    def listar_agendamentos(self):
        return self.__agenda

    def __str__(self):
        return f"Profissional: {self.__nome} ({self.__especialidade}) | Registro: {self.__registro}"

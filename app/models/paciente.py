class Paciente:

    def __init__(self, nome: str, cpf: str, data_nascimento: str, telefone: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
        self.__telefone = telefone
        self.__historico = []  

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome: str):
        if len(novo_nome) < 3:
            raise ValueError("Nome deve conter ao menos 3 caracteres.")
        self.__nome = novo_nome

    def get_cpf(self):
        return self.__cpf

    def get_data_nascimento(self):
        return self.__data_nascimento

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, novo_telefone: str):
        self.__telefone = novo_telefone

    def adicionar_historico(self, descricao: str):
        self.__historico.append(descricao)

    def listar_historico(self):
        return self.__historico

    def __str__(self):
        return f"Paciente: {self.__nome} | CPF: {self.__cpf}"

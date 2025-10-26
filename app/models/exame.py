from datetime import datetime

class Exame:

    def __init__(self, paciente, tipo: str, data_solicitacao: str, profissional=None):
        
        self.__paciente = paciente
        self.__profissional = profissional
        self.__tipo = tipo
        self.__data_solicitacao = data_solicitacao
        self.__resultado = None
        self.__status = "Solicitado"
        self.__data_criacao = datetime.now()

    def get_paciente(self):
        return self.__paciente

    def get_profissional(self):
        return self.__profissional

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, novo_tipo: str):
        self.__tipo = novo_tipo

    def get_data_solicitacao(self):
        return self.__data_solicitacao

    def get_status(self):
        return self.__status

    def set_status(self, novo_status: str):
        if novo_status not in ["Solicitado", "Em andamento", "Concluído"]:
            raise ValueError("Status inválido.")
        self.__status = novo_status

    def get_resultado(self):
        return self.__resultado

    def registrar_resultado(self, resultado: str):
        
        self.__resultado = resultado
        self.__status = "Concluído"

    def __str__(self):
        paciente_nome = self.__paciente.get_nome()
        profissional_nome = self.__profissional.get_nome() if self.__profissional else "Desconhecido"
        return (
            f"Exame: {self.__tipo} | Paciente: {paciente_nome} | "
            f"Profissional: {profissional_nome} | Status: {self.__status}"
        )

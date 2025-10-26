# app/models/agendamento.py
from datetime import datetime

class Agendamento:
    """
    Classe que representa um agendamento de consulta no sistema SUS Digital.
    Faz a composição entre Paciente e Profissional.
    """

    def __init__(self, paciente, profissional, data: str, hora: str):
        """
        :param paciente: objeto da classe Paciente
        :param profissional: objeto da classe Profissional
        :param data: data no formato 'YYYY-MM-DD'
        :param hora: hora no formato 'HH:MM'
        """
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__hora = hora
        self.__status = "Agendado"
        self.__data_criacao = datetime.now()

    # Métodos de acesso
    def get_paciente(self):
        return self.__paciente

    def get_profissional(self):
        return self.__profissional

    def get_data(self):
        return self.__data

    def set_data(self, nova_data: str):
        self.__data = nova_data

    def get_hora(self):
        return self.__hora

    def set_hora(self, nova_hora: str):
        self.__hora = nova_hora

    def get_status(self):
        return self.__status

    def set_status(self, novo_status: str):
        if novo_status not in ["Agendado", "Cancelado", "Concluído"]:
            raise ValueError("Status inválido.")
        self.__status = novo_status

    def get_data_criacao(self):
        return self.__data_criacao

    # Métodos de comportamento
    def cancelar(self):
        self.__status = "Cancelado"

    def concluir(self):
        self.__status = "Concluído"

    def __str__(self):
        return (
            f"Agendamento: {self.__paciente.get_nome()} com "
            f"{self.__profissional.get_nome()} "
            f"em {self.__data} às {self.__hora} - Status: {self.__status}"
        )

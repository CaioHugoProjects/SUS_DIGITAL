from datetime import datetime

class Medicacao:

    def __init__(self, paciente, profissional, nome: str, dosagem: str, frequencia: str, duracao: str):
        
        self.__paciente = paciente
        self.__profissional = profissional
        self.__nome = nome
        self.__dosagem = dosagem
        self.__frequencia = frequencia
        self.__duracao = duracao
        self.__data_prescricao = datetime.now()
        self.__status = "Ativa"

    def get_paciente(self):
        return self.__paciente

    def get_profissional(self):
        return self.__profissional

    def get_nome(self):
        return self.__nome

    def get_dosagem(self):
        return self.__dosagem

    def get_frequencia(self):
        return self.__frequencia

    def get_duracao(self):
        return self.__duracao

    def get_status(self):
        return self.__status

    def get_data_prescricao(self):
        return self.__data_prescricao

    def encerrar_tratamento(self):
        
        self.__status = "Encerrada"

    def __str__(self):
        return (
            f"Medicamento: {self.__nome} ({self.__dosagem}) | "
            f"Paciente: {self.__paciente.get_nome()} | "
            f"Profissional: {self.__profissional.get_nome()} | "
            f"Status: {self.__status}"
        )

from datetime import datetime

class Encaminhamento:

    def __init__(self, paciente, profissional_origem, especialidade_destino: str, motivo: str):
        
        self.__paciente = paciente
        self.__profissional_origem = profissional_origem
        self.__especialidade_destino = especialidade_destino
        self.__motivo = motivo
        self.__data_emissao = datetime.now()
        self.__status = "Emitido"

    def get_paciente(self):
        return self.__paciente

    def get_profissional_origem(self):
        return self.__profissional_origem

    def get_especialidade_destino(self):
        return self.__especialidade_destino

    def set_especialidade_destino(self, nova_especialidade: str):
        self.__especialidade_destino = nova_especialidade

    def get_motivo(self):
        return self.__motivo

    def set_motivo(self, novo_motivo: str):
        self.__motivo = novo_motivo

    def get_status(self):
        return self.__status

    def get_data_emissao(self):
        return self.__data_emissao

    def marcar_como_recebido(self):
        
        self.__status = "Recebido"

    def __str__(self):
        return (
            f"Encaminhamento: {self.__paciente.get_nome()} → {self.__especialidade_destino} | "
            f"Emitido por: {self.__profissional_origem.get_nome()} | "
            f"Status: {self.__status}"
        )

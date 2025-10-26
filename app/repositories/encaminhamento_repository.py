from app.models.encaminhamento import Encaminhamento

class EncaminhamentoRepository:

    def __init__(self):
        self.encaminhamentos = []

    def adicionar(self, encaminhamento: Encaminhamento):
        self.encaminhamentos.append(encaminhamento)

    def listar_todos(self):
        return self.encaminhamentos

    def listar_por_paciente(self, cpf: str):
        return [e for e in self.encaminhamentos if e.get_paciente().get_cpf() == cpf]

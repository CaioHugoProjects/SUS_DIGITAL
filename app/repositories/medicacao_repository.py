from app.models.medicacao import Medicacao

class MedicacaoRepository:

    def __init__(self):
        self.medicacoes = []

    def adicionar(self, medicacao: Medicacao):
        self.medicacoes.append(medicacao)

    def listar_todos(self):
        return self.medicacoes

    def listar_por_paciente(self, cpf: str):
        return [m for m in self.medicacoes if m.get_paciente().get_cpf() == cpf]

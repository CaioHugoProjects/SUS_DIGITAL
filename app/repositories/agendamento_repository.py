from app.models.agendamento import Agendamento

class AgendamentoRepository:

    def __init__(self):
        self.agendamentos = []

    def adicionar(self, agendamento: Agendamento):
        self.agendamentos.append(agendamento)

    def listar_todos(self):
        return self.agendamentos

    def listar_por_paciente(self, cpf: str):
        return [a for a in self.agendamentos if a.get_paciente().get_cpf() == cpf]

    def listar_por_profissional(self, registro: str):
        return [a for a in self.agendamentos if a.get_profissional().get_registro() == registro]

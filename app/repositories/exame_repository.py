from app.models.exame import Exame

class ExameRepository:

    def __init__(self):
        self.exames = []

    def adicionar(self, exame: Exame):
        self.exames.append(exame)

    def listar_todos(self):
        return self.exames

    def listar_por_paciente(self, cpf: str):
        return [e for e in self.exames if e.get_paciente().get_cpf() == cpf]

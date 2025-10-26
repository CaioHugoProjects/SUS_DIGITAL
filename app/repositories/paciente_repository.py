from app.models.paciente import Paciente

class PacienteRepository:

    def __init__(self):
        self.pacientes = []

    def adicionar(self, paciente: Paciente):
        self.pacientes.append(paciente)

    def listar_todos(self):
        return self.pacientes

    def buscar_por_cpf(self, cpf: str):
        for p in self.pacientes:
            if p.get_cpf() == cpf:
                return p
        return None

    def remover_por_cpf(self, cpf: str):
        paciente = self.buscar_por_cpf(cpf)
        if paciente:
            self.pacientes.remove(paciente)
            return True
        return False

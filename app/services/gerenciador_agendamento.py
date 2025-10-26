from datetime import datetime
from app.models.agendamento import Agendamento

class GerenciadorAgendamento:

    def __init__(self, paciente_repo, profissional_repo, agendamento_repo):
        self.paciente_repo = paciente_repo
        self.profissional_repo = profissional_repo
        self.agendamento_repo = agendamento_repo

    def criar_agendamento(self, cpf_paciente: str, registro_profissional: str, data: str, hora: str):
        
        paciente = self.paciente_repo.buscar_por_cpf(cpf_paciente)
        profissional = self.profissional_repo.buscar_por_registro(registro_profissional)

        if not paciente:
            raise ValueError("Paciente não encontrado.")
        if not profissional:
            raise ValueError("Profissional não encontrado.")

        try:
            datetime.strptime(f"{data} {hora}", "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Data ou hora inválida.")

        for ag in self.agendamento_repo.listar_todos():
            if (ag.get_profissional().get_registro() == registro_profissional and
                ag.get_data() == data and
                ag.get_hora() == hora and
                ag.get_status() == "Agendado"):
                raise ValueError("Horário já reservado para este profissional.")

        novo = Agendamento(paciente, profissional, data, hora)
        self.agendamento_repo.adicionar(novo)
        profissional.adicionar_agendamento(novo)
        paciente.adicionar_historico(f"Consulta agendada com {profissional.get_nome()} em {data} às {hora}.")
        return novo

    def cancelar_agendamento(self, cpf_paciente: str, data: str, hora: str):
        
        agendamentos = self.agendamento_repo.listar_por_paciente(cpf_paciente)
        for ag in agendamentos:
            if ag.get_data() == data and ag.get_hora() == hora:
                ag.cancelar()
                ag.get_paciente().adicionar_historico(f"Consulta cancelada: {data} às {hora}")
                return True
        return False

    def listar_agendamentos_por_paciente(self, cpf_paciente: str):
        
        return self.agendamento_repo.listar_por_paciente(cpf_paciente)

    def listar_agendamentos_por_profissional(self, registro: str):
        
        return self.agendamento_repo.listar_por_profissional(registro)

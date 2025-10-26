from app.models.agendamento import Agendamento

class AgendamentoSchema:

    @staticmethod
    def to_dict(agendamento: Agendamento):
        return {
            "paciente": agendamento.get_paciente().get_nome(),
            "profissional": agendamento.get_profissional().get_nome(),
            "data": agendamento.get_data(),
            "hora": agendamento.get_hora(),
            "status": agendamento.get_status()
        }

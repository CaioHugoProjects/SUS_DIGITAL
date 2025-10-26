from app.models.exame import Exame

class ExameSchema:

    @staticmethod
    def to_dict(exame: Exame):
        return {
            "paciente": exame.get_paciente().get_nome(),
            "profissional": exame.get_profissional().get_nome() if exame.get_profissional() else None,
            "tipo": exame.get_tipo(),
            "status": exame.get_status(),
            "resultado": exame.get_resultado(),
            "data_solicitacao": exame.get_data_solicitacao()
        }

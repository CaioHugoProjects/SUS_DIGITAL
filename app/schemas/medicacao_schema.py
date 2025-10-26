from app.models.medicacao import Medicacao

class MedicacaoSchema:

    @staticmethod
    def to_dict(medicacao: Medicacao):
        return {
            "paciente": medicacao.get_paciente().get_nome(),
            "profissional": medicacao.get_profissional().get_nome(),
            "nome": medicacao.get_nome(),
            "dosagem": medicacao.get_dosagem(),
            "frequencia": medicacao.get_frequencia(),
            "duracao": medicacao.get_duracao(),
            "status": medicacao.get_status()
        }

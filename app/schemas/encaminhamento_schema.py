from app.models.encaminhamento import Encaminhamento

class EncaminhamentoSchema:

    @staticmethod
    def to_dict(enc: Encaminhamento):
        return {
            "paciente": enc.get_paciente().get_nome(),
            "profissional_origem": enc.get_profissional_origem().get_nome(),
            "especialidade_destino": enc.get_especialidade_destino(),
            "motivo": enc.get_motivo(),
            "status": enc.get_status(),
            "data_emissao": enc.get_data_emissao().strftime("%Y-%m-%d %H:%M")
        }

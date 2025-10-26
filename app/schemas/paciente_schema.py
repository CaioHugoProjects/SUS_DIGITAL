from app.models.paciente import Paciente

class PacienteSchema:

    @staticmethod
    def to_dict(paciente: Paciente):
        return {
            "nome": paciente.get_nome(),
            "cpf": paciente.get_cpf(),
            "data_nascimento": paciente.get_data_nascimento(),
            "telefone": paciente.get_telefone(),
            "historico": paciente.listar_historico()
        }

    @staticmethod
    def from_dict(data: dict):
        return Paciente(
            nome=data["nome"],
            cpf=data["cpf"],
            data_nascimento=data["data_nascimento"],
            telefone=data["telefone"]
        )

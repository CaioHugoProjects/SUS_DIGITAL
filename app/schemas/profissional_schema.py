from app.models.profissional import Profissional

class ProfissionalSchema:

    @staticmethod
    def to_dict(profissional: Profissional):
        return {
            "nome": profissional.get_nome(),
            "cpf": profissional.get_cpf(),
            "especialidade": profissional.get_especialidade(),
            "registro": profissional.get_registro(),
            "unidade": profissional.get_unidade(),
        }

    @staticmethod
    def from_dict(data: dict):
        return Profissional(
            nome=data["nome"],
            cpf=data["cpf"],
            especialidade=data["especialidade"],
            registro=data["registro"],
            unidade=data["unidade"]
        )

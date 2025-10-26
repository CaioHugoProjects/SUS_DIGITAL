from app.models.profissional import Profissional

class ProfissionalRepository:

    def __init__(self):
        self.profissionais = []

    def adicionar(self, profissional: Profissional):
        self.profissionais.append(profissional)

    def listar_todos(self):
        return self.profissionais

    def buscar_por_registro(self, registro: str):
        for p in self.profissionais:
            if p.get_registro() == registro:
                return p
        return None

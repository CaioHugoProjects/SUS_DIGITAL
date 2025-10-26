import re
from datetime import datetime

class Validador:

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        
        return bool(re.fullmatch(r"\d{11}", cpf))

    @staticmethod
    def validar_data(data: str) -> bool:
        
        try:
            datetime.strptime(data, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def validar_hora(hora: str) -> bool:
        
        return bool(re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", hora))

    @staticmethod
    def validar_telefone(telefone: str) -> bool:
        
        return bool(re.fullmatch(r"\d{10,11}", telefone))

from flask import Blueprint, render_template, request, redirect, url_for
from app.models.paciente import Paciente
from app.repositories.paciente_repository import PacienteRepository
from app.schemas.paciente_schema import PacienteSchema
from app.services.validador import Validador

paciente_bp = Blueprint('paciente', __name__, template_folder='../templates')

paciente_repo = PacienteRepository()

@paciente_bp.route('/pacientes')
def listar_pacientes():
    
    pacientes = paciente_repo.listar_todos()
    pacientes_dict = [PacienteSchema.to_dict(p) for p in pacientes]
    return render_template('paciente.html', pacientes=pacientes_dict)

@paciente_bp.route('/pacientes/novo', methods=['GET', 'POST'])
def cadastrar_paciente():
    
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        data_nascimento = request.form['data_nascimento']
        telefone = request.form['telefone']

        if not nome or not cpf or not data_nascimento or not telefone:
            return "Todos os campos são obrigatórios.", 400

        if not Validador.validar_cpf(cpf):
            return "CPF inválido. Deve conter 11 números.", 400
        if not Validador.validar_data(data_nascimento):
            return "Data de nascimento inválida.", 400
        if not Validador.validar_telefone(telefone):
            return "Telefone inválido.", 400

        paciente = Paciente(nome, cpf, data_nascimento, telefone)
        paciente_repo.adicionar(paciente)
        return redirect(url_for('paciente.listar_pacientes'))

    return render_template('paciente.html', pacientes=paciente_repo.listar_todos(), form=True)

@paciente_bp.route('/pacientes/remover/<cpf>', methods=['POST'])
def remover_paciente(cpf):
    
    sucesso = paciente_repo.remover_por_cpf(cpf)
    if sucesso:
        return redirect(url_for('paciente.listar_pacientes'))
    return "Paciente não encontrado.", 404

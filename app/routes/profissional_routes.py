from flask import Blueprint, render_template, request, redirect, url_for
from app.models.profissional import Profissional
from app.repositories.profissional_repository import ProfissionalRepository
from app.schemas.profissional_schema import ProfissionalSchema
from app.services.validador import Validador

profissional_bp = Blueprint('profissional', __name__, template_folder='../templates')

profissional_repo = ProfissionalRepository()

@profissional_bp.route('/profissionais')
def listar_profissionais():
    
    profissionais = profissional_repo.listar_todos()
    profissionais_dict = [ProfissionalSchema.to_dict(p) for p in profissionais]
    return render_template('profissional.html', profissionais=profissionais_dict)

@profissional_bp.route('/profissionais/novo', methods=['GET', 'POST'])
def cadastrar_profissional():
    
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        especialidade = request.form['especialidade']
        registro = request.form['registro']
        unidade = request.form['unidade']

        if not Validador.validar_cpf(cpf):
            return "CPF inválido. Deve conter 11 números.", 400

        profissional = Profissional(nome, cpf, especialidade, registro, unidade)
        profissional_repo.adicionar(profissional)
        return redirect(url_for('profissional.listar_profissionais'))

    return render_template('profissional.html', profissionais=profissional_repo.listar_todos(), form=True)

@profissional_bp.route('/profissionais/remover/<registro>', methods=['POST'])
def remover_profissional(registro):
    
    prof = profissional_repo.buscar_por_registro(registro)
    if prof:
        profissional_repo.profissionais.remove(prof)
        return redirect(url_for('profissional.listar_profissionais'))
    return "Profissional não encontrado.", 404

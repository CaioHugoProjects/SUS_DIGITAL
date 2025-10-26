from flask import Blueprint, render_template, request, redirect, url_for
from app.models.exame import Exame
from app.repositories.exame_repository import ExameRepository
from app.repositories.paciente_repository import PacienteRepository
from app.repositories.profissional_repository import ProfissionalRepository
from app.schemas.exame_schema import ExameSchema

exame_bp = Blueprint('exame', __name__, template_folder='../templates')

exame_repo = ExameRepository()
paciente_repo = PacienteRepository()
profissional_repo = ProfissionalRepository()

@exame_bp.route('/exames')
def listar_exames():
    
    exames = exame_repo.listar_todos()
    exames_dict = [ExameSchema.to_dict(e) for e in exames]
    return render_template('exame.html', exames=exames_dict)

@exame_bp.route('/exames/novo', methods=['GET', 'POST'])
def solicitar_exame():
    
    if request.method == 'POST':
        cpf_paciente = request.form['cpf_paciente']
        registro_profissional = request.form['registro_profissional']
        tipo = request.form['tipo']
        data_solicitacao = request.form['data_solicitacao']

        paciente = paciente_repo.buscar_por_cpf(cpf_paciente)
        profissional = profissional_repo.buscar_por_registro(registro_profissional)

        if not paciente or not profissional:
            return "Paciente ou profissional não encontrado.", 404

        exame = Exame(paciente, tipo, data_solicitacao, profissional)
        exame_repo.adicionar(exame)
        paciente.adicionar_historico(f"Exame solicitado: {tipo} em {data_solicitacao}")
        return redirect(url_for('exame.listar_exames'))

    return render_template('exame.html', form=True)

@exame_bp.route('/exames/resultado', methods=['POST'])
def registrar_resultado():
    
    tipo = request.form['tipo']
    cpf_paciente = request.form['cpf_paciente']
    resultado = request.form['resultado']

    exames = exame_repo.listar_por_paciente(cpf_paciente)
    for e in exames:
        if e.get_tipo() == tipo and e.get_status() == "Solicitado":
            e.registrar_resultado(resultado)
            e.get_paciente().adicionar_historico(f"Resultado registrado para exame: {tipo}")
            return redirect(url_for('exame.listar_exames'))

    return "Exame não encontrado ou já concluído.", 404

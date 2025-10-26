from flask import Blueprint, render_template, request, redirect, url_for
from app.models.encaminhamento import Encaminhamento
from app.repositories.encaminhamento_repository import EncaminhamentoRepository
from app.repositories.paciente_repository import PacienteRepository
from app.repositories.profissional_repository import ProfissionalRepository
from app.schemas.encaminhamento_schema import EncaminhamentoSchema

encaminhamento_bp = Blueprint('encaminhamento', __name__, template_folder='../templates')

encaminhamento_repo = EncaminhamentoRepository()
paciente_repo = PacienteRepository()
profissional_repo = ProfissionalRepository()

@encaminhamento_bp.route('/encaminhamentos')
def listar_encaminhamentos():
    
    encaminhamentos = encaminhamento_repo.listar_todos()
    enc_dict = [EncaminhamentoSchema.to_dict(e) for e in encaminhamentos]
    return render_template('encaminhamento.html', encaminhamentos=enc_dict)

@encaminhamento_bp.route('/encaminhamentos/novo', methods=['GET', 'POST'])
def emitir_encaminhamento():
    
    if request.method == 'POST':
        cpf_paciente = request.form['cpf_paciente']
        registro_profissional = request.form['registro_profissional']
        especialidade_destino = request.form['especialidade_destino']
        motivo = request.form['motivo']

        paciente = paciente_repo.buscar_por_cpf(cpf_paciente)
        profissional = profissional_repo.buscar_por_registro(registro_profissional)

        if not paciente or not profissional:
            return "Paciente ou profissional não encontrado.", 404

        encaminhamento = Encaminhamento(paciente, profissional, especialidade_destino, motivo)
        encaminhamento_repo.adicionar(encaminhamento)
        paciente.adicionar_historico(f"Encaminhamento emitido para {especialidade_destino}.")
        return redirect(url_for('encaminhamento.listar_encaminhamentos'))

    return render_template('encaminhamento.html', form=True)

@encaminhamento_bp.route('/encaminhamentos/receber', methods=['POST'])
def receber_encaminhamento():
    
    cpf_paciente = request.form['cpf_paciente']
    especialidade_destino = request.form['especialidade_destino']

    encs = encaminhamento_repo.listar_por_paciente(cpf_paciente)
    for e in encs:
        if e.get_especialidade_destino() == especialidade_destino and e.get_status() == "Emitido":
            e.marcar_como_recebido()
            e.get_paciente().adicionar_historico(f"Encaminhamento recebido: {especialidade_destino}")
            return redirect(url_for('encaminhamento.listar_encaminhamentos'))

    return "Encaminhamento não encontrado ou já recebido.", 404

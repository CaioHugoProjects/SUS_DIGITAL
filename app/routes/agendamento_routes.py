# app/routes/agendamento_routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.repositories.paciente_repository import PacienteRepository
from app.repositories.profissional_repository import ProfissionalRepository
from app.repositories.agendamento_repository import AgendamentoRepository
from app.schemas.agendamento_schema import AgendamentoSchema
from app.services.gerenciador_agendamento import GerenciadorAgendamento

# Cria o módulo de rotas (Blueprint)
agendamento_bp = Blueprint('agendamento', __name__, template_folder='../templates')

# Repositórios (em memória)
paciente_repo = PacienteRepository()
profissional_repo = ProfissionalRepository()
agendamento_repo = AgendamentoRepository()

# Serviço principal
gerenciador = GerenciadorAgendamento(paciente_repo, profissional_repo, agendamento_repo)

@agendamento_bp.route('/agendamentos')
def listar_agendamentos():
    """Lista todos os agendamentos realizados."""
    agendamentos = agendamento_repo.listar_todos()
    agendamentos_dict = [AgendamentoSchema.to_dict(a) for a in agendamentos]
    return render_template('agendamento.html', agendamentos=agendamentos_dict)

@agendamento_bp.route('/agendamentos/novo', methods=['GET', 'POST'])
def criar_agendamento():
    """Cria um novo agendamento de consulta."""
    if request.method == 'POST':
        cpf_paciente = request.form['cpf_paciente']
        registro_profissional = request.form['registro_profissional']
        data = request.form['data']
        hora = request.form['hora']

        try:
            gerenciador.criar_agendamento(cpf_paciente, registro_profissional, data, hora)
        except ValueError as e:
            return f"Erro: {e}", 400

        return redirect(url_for('agendamento.listar_agendamentos'))

    # Exibe formulário
    return render_template('agendamento.html', form=True)

@agendamento_bp.route('/agendamentos/cancelar', methods=['POST'])
def cancelar_agendamento():
    """Cancela um agendamento específico."""
    cpf_paciente = request.form['cpf_paciente']
    data = request.form['data']
    hora = request.form['hora']

    sucesso = gerenciador.cancelar_agendamento(cpf_paciente, data, hora)
    if sucesso:
        return redirect(url_for('agendamento.listar_agendamentos'))
    return "Agendamento não encontrado.", 404

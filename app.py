from flask import Flask, render_template
from app.routes.paciente_routes import paciente_bp
from app.routes.profissional_routes import profissional_bp
from app.routes.agendamento_routes import agendamento_bp
from app.routes.exame_routes import exame_bp
from app.routes.encaminhamento_routes import encaminhamento_bp

app = Flask(__name__)

app.register_blueprint(paciente_bp)
app.register_blueprint(profissional_bp)
app.register_blueprint(agendamento_bp)
app.register_blueprint(exame_bp)
app.register_blueprint(encaminhamento_bp)

@app.route('/')
def index():
    return render_template('index.html', titulo="SUS Digital")

if __name__ == '__main__':
    app.run(debug=True)

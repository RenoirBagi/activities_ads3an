from flask_sqlalchemy import SQLAlchemy
from config import db, app
from controllers.atividade_controller import atividade_bp

app.register_blueprint(atividade_bp)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

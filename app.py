from flask import Flask
from config import Config
from db import db
from routes.veiculo_routes import veiculos_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(veiculos_bp)

if __name__ == '__main__':
    app.run(debug=True)

# -*- coding: utf-8 -*-
from app import create_app, db
from flask_migrate import Migrate

app = create_app()

# Configuração do Migrate
migrate = Migrate(app, db)

if __name__ == "__main__":
    # Executa o servidor Flask no modo de desenvolvimento
    app.run(host="0.0.0.0", port=5000, debug=True)

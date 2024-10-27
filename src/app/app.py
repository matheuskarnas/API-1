from flask import Flask
from back.routes.vereadorPageRoute import vereadorPage

def create_app():
    app = Flask(__name__, template_folder='front/templates', static_folder='front/static')
    
    app.register_blueprint(vereadorPage)  # Registrando o blueprint

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8000)

from flask import Flask, url_for, render_template

# Inicialização do Flask! Sempre manter no topo após importações.
app = Flask(
  __name__, template_folder="front/templates", static_folder="front/static"
  )

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/information.html")
def information():
  return render_template('information.html')

# Criação de Rotas
app.run(debug=True)
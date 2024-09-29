from flask import Flask, url_for, render_template

# Inicialização do Flask! Sempre manter no topo após importações.
app = Flask(
  __name__, template_folder="front/templates", static_folder="front/static"
  )

# Criação de Rotas
@app.route("/")
def home():
  return render_template('index.html')

@app.route("/information.html")
def information():
  return render_template('information.html')

@app.route("/comp_vereador.html")
def comp_vereador():
  return render_template('comp_vereador.html')

@app.route("/teste.html")
def teste():
  return render_template('teste.html')

app.run(debug=True)


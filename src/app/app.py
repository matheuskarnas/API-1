from flask import Flask, url_for, render_template

# Inicialização do Flask! Sempre manter no topo após importações.
app = Flask(
  __name__, template_folder="front/templates", static_folder="front/static"
  )

# ROTA PARA PÁGINA INDEX
@app.route("/")
def home():
  return render_template('index.html')


# ROTA PARA PÁGINA DE INFORMAÇÃO
@app.route("/informationPage.html")
def information():
  return render_template('informationPage.html')

# ROTA PARA PÁGINA DE COMPARAÇÃO
@app.route("/comparationPage.html")
def comp_vereador():
  return render_template('comparationPage.html')

app.run(debug=True)


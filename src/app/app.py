import asyncio
from flask import Flask, render_template, send_file
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

# Set the event loop policy to avoid zmq warnings on Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Initialize Flask app
app = Flask(_name_, template_folder="front/templates", static_folder="front/static")

# Path to the notebook and the generated HTML
NOTEBOOK_PATH = r"./src/app/back/graficos.ipynb"
GENERATED_HTML_PATH = r"./src/app/front/static/grafico.html"

def execute_notebook(notebook_path):
    """Execute the notebook and return True if successful, False otherwise."""
    try:
        with open(notebook_path) as f:
            notebook = nbformat.read(f, as_version=4)

        notebook_dir = os.path.dirname(notebook_path)

        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(notebook, {"metadata": {"path": notebook_dir}})

        print("Notebook executed successfully.")
        return True
    except Exception as e:
        print(f"Error executing notebook: {str(e)}")
        return False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/informationPage.html")
def information():
    success = execute_notebook(NOTEBOOK_PATH)

    if success:
        print("Notebook executed and HTML generated.")
    else:
        print("Failed to execute notebook.")

    if os.path.exists(GENERATED_HTML_PATH):
        return render_template("informationPage.html")
    else:
        return "<p>Failed to generate grafico.html. Check the logs for details.</p>"

@app.route("/comparationPage.html")
def comp_vereador():
    return render_template("comparationPage.html")

if _name_ == "_main_":
    app.run(debug=True)
  
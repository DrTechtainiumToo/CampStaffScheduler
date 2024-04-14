from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_program', methods=['POST'])
def run_program():
    try:
        # Assuming your Python code is in a script named 'script.py'
        output = subprocess.run(['python', 'script.py'], capture_output=True, text=True)
        return f"<h1>Output</h1><pre>{output.stdout}</pre>"
    except Exception as e:
        return f"<h1>Error</h1><pre>{e}</pre>"

if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-data')
def get_data():
    # Simulate data fetching
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
#thanks GPT for getting me started 
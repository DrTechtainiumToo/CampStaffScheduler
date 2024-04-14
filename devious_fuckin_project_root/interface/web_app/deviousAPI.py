from flask import Flask, jsonify, request

#backendshit???

#python filename.py
#GUI - API - SERVER STUFF
#http://localhost:5000/



app = Flask(__name__)

# API Endpoints:


# A simple in-memory data store for the example
tasks = [
    {'id': 1, 'title': 'Do laundry', 'completed': False},
    {'id': 2, 'title': 'Write blog post', 'completed': False}
]


@app.route('/')
def index():
    return render_template('index.html')


# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Route to get a single task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is not None:
        return jsonify(task)
    else:
        return jsonify({'message': 'task not found'}), 404

# Route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        return jsonify({'message': 'Bad request'}), 400
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'completed': False
    }
    tasks.append(task)
    return jsonify(task), 201

# Route to update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'task not found'}), 404
    task['title'] = request.json.get('title', task['title'])
    task['completed'] = request.json.get('completed', task['completed'])
    return jsonify(task)

# Route to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'task deleted'})

if __name__ == '__main__':
    app.run(debug=True)


'''
def run_cli():
    pass
#command line interface

if __name__ == "__main__":
    run_cli()
#app_backend.py

from flask import Flask, jsonify,request
app = Flask(__name__)

#@app.route
#HTTP endpoint logic

#star server
if __name__ == "__main__":
    app.run(debug=True, port='0.0.0.0', port=5000)

"""POST = send new data
GET = retreive
PUT or PATCH to update existing data
DELETE to remove data"""
'''
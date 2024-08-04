from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

def load_tasks():
    with open('tasks.json', 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    return jsonify(task)

@app.route('/task', methods=['POST'])
def add_task():
    new_task = request.json
    new_task['id'] = max(task['id'] for task in tasks) + 1 if tasks else 1
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201

@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return '', 204

@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    updated_task = request.json
    for task in tasks:
        if task['id'] == task_id:
            task.update(updated_task)
            save_tasks(tasks)
            return jsonify(task)
    return '', 404

if __name__ == '__main__':
    app.run(debug=True)

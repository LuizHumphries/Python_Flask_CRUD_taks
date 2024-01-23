from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete 

tasks = []
task_id_control = 1


@app.route('/tasks', methods=['POST'])
def create_task():
    """Simple task creation"""
    global task_id_control
    data = request.get_json()
    new_task = Task(task_id=task_id_control, title=data["title"], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """ Get tasks method """
    task_list = [task.to_dict() for task in tasks]
    output = {
        "tasks": task_list,
        "total_tasks": len(tasks)
    }
    return jsonify(output)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get specific task"""    
    for task in tasks:
        if task.task_id == task_id:
            return jsonify(task.to_dict())

    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = None
    for t in tasks:
        if t.task_id == task_id:
            task = t
    
    print(task)
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})



if __name__ == "__main__":
    app.run(debug=True)

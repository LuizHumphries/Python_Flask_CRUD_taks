from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete 

tasks = []
TASK_ID_CONTROL = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    """Simple task creation"""
    global TASK_ID_CONTROL
    data = request.get_json()
    new_task = Task(task_id=TASK_ID_CONTROL, title=data["title"], description=data.get("description", ""))
    TASK_ID_CONTROL += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso", "task_id": new_task.task_id})

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
    """update task"""
    task = None
    for t in tasks:
        if t.task_id == task_id:
            task = t
            break
    
    print(task)
    if not task:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """delete task"""
    task = None
    for t in tasks:
        if t.task_id == task_id:
            task = t
            break
    
    if not task:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)

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


if __name__ == "__main__":
    app.run(debug=True)

class Task:
    """ General Task """
    def __init__(self, task_id, title, description, completed = False) -> None:
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
    
    def to_dict(self):
        """ Return the class arguments as a dict """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
class Taskmaster():
    def __init__(self):
        self._tasklist = []
        self._completed_tasks = []

    def add_todo(self, todo):
        if todo.strip() == "":
            raise Exception("Please add a valid task!")
        self._tasklist.append(todo)

    def track_todos(self):
        return self._tasklist
    
    def mark_complete(self, todo):
        if todo in self._tasklist:
            self._tasklist.remove(todo)
            self._completed_tasks.append(todo)
        else:
            raise Exception("There are no tasks set, so none can be removed. Set up a task to do!")
    
    def track_completed_tasks(self):
        return self._completed_tasks
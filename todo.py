import datetime
import psycopg

class Task:
    def __init__(self, id: int, text: str, status: bool, date: datetime):
        self.id = id 
        self.text = text
        self.status = False 
        self.date = date
    
    def __str__(self):
        return f"ID: {self.id}, Completed: {self.status}, Date: {self.date}, To-Do: {self.text}"

    def complete(self):
        self.status = True


class Todo_List:
    def __init__(self, db):
        self.tasks: list[Task] = []
        self.db = db
    
    def add(self, task: Task):
        new_id = self.db.insert(task)
        task.id = new_id
        self.tasks.append(task)

    def print(self):
        self.read_db()
        for task in self.tasks:
            print(task)

    def read_db(self):
        self.tasks.clear()
        self.tasks = self.db.read()
   

       


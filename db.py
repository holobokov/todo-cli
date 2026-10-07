import psycopg
from todo import Task

class DBManager:
    def __init__(self, host: str, user: str):
        self.conn = psycopg.connect(host=host, user=user, dbname="todo")
        self.init_table()

    def init_table(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                create table if not exists tasks (
                    id serial primary key,
                    text varchar(100),
                    status boolean,
                    date timestamp
                );
            """) 
            self.conn.commit()

    def insert(self, task):
        with self.conn.cursor() as cur:
            cur.execute("insert into tasks (text, status, date) values (%s, %s, %s) returning id;", (task.text, task.status, task.date))
            new_id = cur.fetchone()[0]
            self.conn.commit()
            return new_id

    def read(self):
        task_list = []
        with self.conn.cursor() as cur:
            cur.execute("select * from tasks;")
            for row in cur:
                task_list.append(Task(row[0], row[1], row[2], row[3]))
        return task_list
          
                

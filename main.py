import datetime
import argparse
from todo import Task, Todo_List
from db import DBManager
import psycopg 

def parse_args():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")   

    parser_add = subparser.add_parser("add")
    parser_add.add_argument("description")

    parser_update = subparser.add_parser("update")
    parser_update.add_argument("id", type=int)
    parser_update.add_argument("new_description")

    parser_list = subparser.add_parser("list")

    return parser.parse_args()

def process_args(args):
    if args.command == "add":
        new_task = Task(None, args.description, False, datetime.datetime.now())
        todo.add(new_task)
    elif args.command == "update":
        for task in todo.tasks:
            if task.id == args.id:
                task.text = args.new_description
    elif args.command == "list":



if __name__ == "__main__":
    db = DBManager(host="localhost", user="holobokov")

    todo = Todo_List(db)

    args = parse_args()
    process_args(args)

    todo.read_db()
    todo.print()









import argparse
from core.use_cases import TaskManager
from adapters.database import SQLiteTaskRepo

from adapters.database import SQLiteTaskRepo
from core.use_cases import TaskManager
from logger_config import logger
from datetime import datetime



def main():
    try:
        parser = argparse.ArgumentParser(description="Task Manager CLI")
        parser.add_argument("--add", nargs=4, metavar=("TITLE", "DESCRIPTION", "PRIORITY", "DUE_DATE"), help="Add a new task")
        parser.add_argument("--list", action="store_true", help="List all tasks")
        parser.add_argument("--complete", type=int, metavar="TASK_ID", help="Mark a task as completed")

        args = parser.parse_args()
        db_path = "tasks.db"  
        task_repo = SQLiteTaskRepo(db_path)
        task_manager = TaskManager(task_repo)

        if args.add:
            title, description, priority, due_date = args.add
            task = task_manager.add_task(title, description, int(priority), due_date=datetime.strptime(due_date, "%Y-%m-%d"))
            logger.info(f"Task added: [ID: {task.id}] Title: '{task.title}', Description: '{task.description}', Priority: {task.priority}, Due Date: {task.due_date}")
        
        elif args.list:
            tasks = task_manager.list_tasks()
            if not tasks: logger.info("No tasks found.")
            for task in tasks:
                status = "✓" if task.is_completed else "✗"
                logger.info(f"[{status}] [ID: {task.id}] Title: '{task.title}', Priority: {task.priority}, Due Date: {task.due_date}")
        
        elif args.complete:
            task_manager.complete_task(args.complete)
            print("Task completed.")

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)    

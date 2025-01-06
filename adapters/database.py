import sqlite3
from core.entities import Task
from logger_config import logger

class SQLiteTaskRepo:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            priority INTEGER,
            due_date TEXT,
            is_completed INTEGER
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def next_id(self):
        query = "SELECT COALESCE(MAX(id), 0) + 1 FROM tasks"
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            next_id = cursor.fetchone()[0]
        return next_id    

    def save(self, task):
        try:
            query = "INSERT INTO tasks (id, title, description, priority, due_date, is_completed) VALUES (?, ?, ?, ?, ?, ?)"
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    query,
                    (
                        task.id,
                        task.title,
                        task.description,
                        task.priority,
                        task.due_date.isoformat() if task.due_date else None,  
                        int(task.is_completed)
                    )
                )
        except sqlite3.Error as e:
            logger.error(f"Database error while saving task: {e}")
            raise
        

    def get_all(self):
        query = "SELECT id, title, description, priority, due_date, is_completed FROM tasks"
        result = self.connection.execute(query).fetchall()
        return [
            Task(
                id=row[0],
                title=row[1],
                description=row[2],
                priority=row[3],
                due_date=row[4],
                is_completed=bool(row[5])
            )
            for row in result
        ]

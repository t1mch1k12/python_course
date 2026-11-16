"""
Точка входа в приложение.
"""

from task_manager import TaskManager

if __name__ == "__main__":
    app = TaskManager(storage_path="tasks.json")
    app.run()

"""
Модуль StorageManager — отвечает за хранение задач в JSON-файле.
Ничего не знает об интерфейсе, работает только с данными.
"""

import json
import os

from task import Task


class StorageManager:
    """Загрузка, сохранение и CRUD-операции над задачами в JSON-файле."""

    def __init__(self, filepath="tasks.json"):
        self.filepath = filepath
        self.tasks = []
        self.load()

    def load(self):
        """Загружает список задач из файла. Если файла нет — начинает с пустого списка."""
        if not os.path.exists(self.filepath):
            self.tasks = []
            return self.tasks

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                raw = json.load(f)
            self.tasks = [Task.from_dict(item) for item in raw]
        except (json.JSONDecodeError, OSError):
            self.tasks = []

        return self.tasks

    def save(self):
        """Сохраняет текущий список задач в файл."""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tasks], f, ensure_ascii=False, indent=2)

    def _next_id(self):
        if not self.tasks:
            return 1
        return max(t.id for t in self.tasks) + 1

    def add(self, task):
        """Добавляет новую задачу, присваивает ей id и сохраняет."""
        task.id = self._next_id()
        self.tasks.append(task)
        self.save()
        return task

    def update(self, task_id, **fields):
        """Обновляет поля задачи по id. Возвращает True, если задача найдена."""
        task = self.get(task_id)
        if task is None:
            return False
        for key, value in fields.items():
            if hasattr(task, key):
                setattr(task, key, value)
        self.save()
        return True

    def delete(self, task_id):
        """Удаляет задачу по id. Возвращает True, если задача была найдена и удалена."""
        task = self.get(task_id)
        if task is None:
            return False
        self.tasks.remove(task)
        self.save()
        return True

    def get(self, task_id):
        """Возвращает задачу по id или None."""
        return next((t for t in self.tasks if t.id == task_id), None)

    def get_all(self):
        """Возвращает список всех задач."""
        return self.tasks

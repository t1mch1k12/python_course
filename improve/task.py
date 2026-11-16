"""
Модуль с классом Task — моделью одной задачи.
"""

from datetime import datetime


class Task:
    """Представляет одну задачу в менеджере задач."""

    def __init__(self, title, description="", status=False, author="",
                 id=None, created_at=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status  # False = не выполнена, True = выполнена
        self.author = author
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Преобразует задачу в словарь для сохранения в JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "author": self.author,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        """Создаёт объект Task из словаря (например, прочитанного из JSON)."""
        return cls(
            id=data.get("id"),
            title=data.get("title", ""),
            description=data.get("description", ""),
            status=data.get("status", False),
            author=data.get("author", ""),
            created_at=data.get("created_at"),
        )

    def __repr__(self):
        mark = "✓" if self.status else "✗"
        return f"[{mark}] #{self.id} {self.title} (автор: {self.author})"

"""
Модуль TaskManager — фасад приложения.
Связывает StorageManager (данные) и Interface (отображение/ввод),
реализует CRUD-операции и запускает приложение.
"""

from task import Task
from storage_manager import StorageManager
from interface import Interface


class TaskManager:
    """Фасад: соединяет хранилище и интерфейс, реализует CRUD над задачами."""

    def __init__(self, storage_path="tasks.json"):
        self.storage = StorageManager(storage_path)
        self.interface = Interface()

        # подключаем колбэки интерфейса к методам фасада
        self.interface.on_create = self.create_task
        self.interface.on_edit = self.edit_task
        self.interface.on_delete = self.delete_task
        self.interface.on_toggle = self.toggle_status

    # --- CRUD ---

    def create_task(self):
        """Создаёт новую задачу на основе ввода пользователя."""
        title = self.interface.get_input("Название задачи:")
        if not title:
            return
        description = self.interface.get_input("Описание (можно пусто):") or ""
        author = self.interface.get_input("Автор задачи:") or "неизвестно"

        task = Task(title=title, description=description, author=author)
        self.storage.add(task)
        self.refresh()

    def edit_task(self, index):
        """Редактирует задачу, выбранную по индексу в списке."""
        task = self.storage.get_all()[index]

        new_title = self.interface.get_input("Новое название:", task.title)
        if new_title is None:
            return
        new_description = self.interface.get_input("Новое описание:", task.description)
        if new_description is None:
            return

        self.storage.update(task.id, title=new_title, description=new_description)
        self.refresh()

    def delete_task(self, index):
        """Удаляет задачу, выбранную по индексу, после подтверждения."""
        task = self.storage.get_all()[index]
        if self.interface.ask_confirm(f"Удалить задачу «{task.title}»?"):
            self.storage.delete(task.id)
            self.refresh()

    def toggle_status(self, index):
        """Переключает статус (выполнена/не выполнена) задачи по индексу."""
        task = self.storage.get_all()[index]
        self.storage.update(task.id, status=not task.status)
        self.refresh()

    # --- вспомогательное ---

    def refresh(self):
        """Обновляет отображаемый список задач."""
        self.interface.show_tasks(self.storage.get_all())

    def run(self):
        """Строит интерфейс, отображает задачи и запускает приложение."""
        self.interface.build()
        self.refresh()
        self.interface.run()

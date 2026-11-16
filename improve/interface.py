"""
Модуль Interface — прослойка над tkinter.
Ничего не знает о хранилище данных: только строит окно, показывает задачи
и собирает ввод пользователя. Вся бизнес-логика — в TaskManager.
"""

import tkinter as tk
from tkinter import simpledialog, messagebox

from components import AppButton, AppLabel, AppEntry, AppListbox


class Interface:
    """Отвечает за построение окна и взаимодействие с пользователем."""

    def __init__(self, title="Task Manager v0.2.0"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("520x480")
        self.root.configure(bg="#1e1e2e")

        self.listbox = None

        # callbacks, которые установит TaskManager (фасад)
        self.on_create = None
        self.on_edit = None
        self.on_delete = None
        self.on_toggle = None

    def build(self):
        """Строит все виджеты окна."""
        AppLabel(
            self.root, text="Менеджер задач", bold=True,
            bg="#1e1e2e", fg="white"
        ).pack(pady=(15, 5))

        self.listbox = AppListbox(self.root, width=60, height=15)
        self.listbox.pack(padx=15, pady=5, fill="both", expand=True)
        self.listbox.bind("<Double-Button-1>", lambda e: self._toggle_selected())

        btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame.pack(pady=10)

        AppButton(btn_frame, text="+ Новая", command=self._create_clicked).grid(
            row=0, column=0, padx=5
        )
        AppButton(btn_frame, text="Изменить", command=self._edit_clicked).grid(
            row=0, column=1, padx=5
        )
        AppButton(btn_frame, text="Готово/Не готово", command=self._toggle_selected).grid(
            row=0, column=2, padx=5
        )
        AppButton(btn_frame, text="Удалить", command=self._delete_clicked).grid(
            row=0, column=3, padx=5
        )

        return self

    # --- получение выбранного элемента ---

    def _selected_index(self):
        selection = self.listbox.curselection()
        return selection[0] if selection else None

    # --- обработчики кликов, которые дёргают колбэки фасада ---

    def _create_clicked(self):
        if self.on_create:
            self.on_create()

    def _edit_clicked(self):
        index = self._selected_index()
        if index is None:
            self.show_message("Выберите задачу для изменения.")
            return
        if self.on_edit:
            self.on_edit(index)

    def _delete_clicked(self):
        index = self._selected_index()
        if index is None:
            self.show_message("Выберите задачу для удаления.")
            return
        if self.on_delete:
            self.on_delete(index)

    def _toggle_selected(self):
        index = self._selected_index()
        if index is None:
            return
        if self.on_toggle:
            self.on_toggle(index)

    # --- публичный API, которым пользуется TaskManager ---

    def get_input(self, prompt, initial_value=""):
        """Запрашивает у пользователя строку текста. Возвращает None при отмене."""
        return simpledialog.askstring("Ввод", prompt, initialvalue=initial_value, parent=self.root)

    def ask_confirm(self, message):
        """Запрашивает подтверждение действия. Возвращает True/False."""
        return messagebox.askyesno("Подтверждение", message, parent=self.root)

    def show_message(self, message):
        """Показывает информационное сообщение."""
        messagebox.showinfo("Менеджер задач", message, parent=self.root)

    def show_tasks(self, tasks):
        """Отрисовывает список задач в listbox."""
        self.listbox.delete(0, tk.END)
        for task in tasks:
            mark = "✔" if task.status else "◻"
            self.listbox.insert(tk.END, f"{mark} #{task.id} {task.title} — {task.author}")

    def run(self):
        """Запускает главный цикл окна."""
        self.root.mainloop()

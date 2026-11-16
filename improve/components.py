"""
Модуль с компонентами интерфейса — наследниками стандартных tkinter-виджетов.
Задают единый стиль для всего приложения.
"""

import tkinter as tk
from tkinter import ttk

FONT = ("Segoe UI", 11)
FONT_BOLD = ("Segoe UI", 11, "bold")


class AppButton(tk.Button):
    """Стилизованная кнопка."""

    def __init__(self, master, text="", command=None, **kwargs):
        super().__init__(
            master,
            text=text,
            command=command,
            font=FONT,
            bg="#4a7dfc",
            fg="white",
            activebackground="#3a63d6",
            activeforeground="white",
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2",
            **kwargs,
        )


class AppLabel(tk.Label):
    """Стилизованная надпись."""

    def __init__(self, master, text="", bold=False, **kwargs):
        super().__init__(
            master,
            text=text,
            font=FONT_BOLD if bold else FONT,
            **kwargs,
        )


class AppEntry(tk.Entry):
    """Стилизованное поле ввода."""

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            font=FONT,
            relief="solid",
            bd=1,
            **kwargs,
        )

    def get_value(self):
        return self.get().strip()

    def set_value(self, value):
        self.delete(0, tk.END)
        self.insert(0, value)


class AppListbox(tk.Listbox):
    """Стилизованный список задач."""

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            font=FONT,
            selectmode=tk.SINGLE,
            activestyle="none",
            relief="solid",
            bd=1,
            **kwargs,
        )

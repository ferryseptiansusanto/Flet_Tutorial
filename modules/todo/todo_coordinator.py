# ---- file: modules/todo/todo_coordinator.py ----
import flet as ft
from modules.todo.todo_state import TodoState
from modules.todo.todo_logic import TodoLogic
from modules.todo.todo_view import TodoView

class TodoCoordinator:
    def __init__(self):
        self.state = TodoState()
        self.logic = TodoLogic(state=self.state)
        self.view = TodoView(logic=self.logic)
        self.logic.on_change = self.view.render
        self.logic.load_initial_data()

    def get_view(self) -> ft.Control:
        return self.view
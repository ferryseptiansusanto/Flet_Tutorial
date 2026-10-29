# ---- file: modules/todo/todo_logic.py ----
from typing import Callable, Optional
from model.models import TodoModel, TodoORM
from modules.todo.todo_state import TodoState

class TodoLogic:
    def __init__(self, state: TodoState, on_change: Optional[Callable[[], None]] = None):
        self.state = state
        self.on_change = on_change

    def _notify(self) -> None:
        if self.on_change: self.on_change()

    def load_initial_data(self) -> None:
        self.state.tasks = TodoORM.get_all()
        self._notify()

    def set_new_task_input(self, value: str) -> None:
        self.state.new_task_input = value

    def set_filter(self, status: str) -> None:
        self.state.filter_status = status
        self._notify()

    def add_task(self) -> None:
        task_name = self.state.new_task_input.strip()
        if not task_name: return
        
        new_task = TodoModel(task_name=task_name)
        TodoORM.insert(new_task)
        
        self.state.tasks.append(new_task)
        self.state.new_task_input = ""
        self._notify()

    def toggle_task(self, task_id: str, completed: bool) -> None:
        for t in self.state.tasks:
            if t.id == task_id:
                t.completed = completed
                TodoORM.update(t)
                break
        self._notify()

    def update_task_name(self, task_id: str, new_name: str) -> None:
        for t in self.state.tasks:
            if t.id == task_id:
                t.task_name = new_name
                TodoORM.update(t)
                break
        self._notify()

    def delete_task(self, task_id: str) -> None:
        TodoORM.delete(task_id)
        self.state.tasks = [t for t in self.state.tasks if t.id != task_id]
        self._notify()
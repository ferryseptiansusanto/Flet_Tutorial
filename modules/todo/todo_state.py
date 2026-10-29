# ---- file: modules/todo/todo_state.py ----
from dataclasses import dataclass, field
from typing import List
from model.models import TodoModel

@dataclass
class TodoState:
    tasks: List[TodoModel] = field(default_factory=list)
    filter_status: str = "all"
    new_task_input: str = ""
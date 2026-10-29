# ---- file: Model/models.py ----
import uuid
from dataclasses import dataclass, field
from typing import List

@dataclass
class TodoModel:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    task_name: str = ""
    completed: bool = False

class TodoORM:
    _db_table: List[TodoModel] = []

    @classmethod
    def get_all(cls) -> List[TodoModel]:
        return [TodoModel(id=t.id, task_name=t.task_name, completed=t.completed) for t in cls._db_table]

    @classmethod
    def insert(cls, task: TodoModel) -> None:
        cls._db_table.append(task)

    @classmethod
    def update(cls, updated_task: TodoModel) -> None:
        for i, t in enumerate(cls._db_table):
            if t.id == updated_task.id:
                cls._db_table[i] = updated_task
                break

    @classmethod
    def delete(cls, task_id: str) -> None:
        cls._db_table = [t for t in cls._db_table if t.id != task_id]
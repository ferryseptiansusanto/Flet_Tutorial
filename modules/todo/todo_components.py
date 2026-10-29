# ---- file: modules/todo/todo_components.py ----
from typing import Callable
import flet as ft
from model.models import TodoModel

class TodoTaskItem(ft.Column):
    def __init__(self, task: TodoModel, on_status_change: Callable[[str, bool], None], on_update_name: Callable[[str, str], None], on_delete: Callable[[str], None]):
        super().__init__()
        self.task = task
        self.on_status_change = on_status_change
        self.on_update_name = on_update_name
        self.on_delete = on_delete

        self.display_task = ft.Checkbox(value=self.task.completed, label=self.task.task_name, on_change=lambda e: self.on_status_change(self.task.id, e.control.value))
        
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(icon=ft.Icons.CREATE_OUTLINED, on_click=self._edit_clicked),
                        ft.IconButton(icon=ft.Icons.DELETE_OUTLINE, on_click=lambda _: self.on_delete(self.task.id)),
                    ],
                ),
            ],
        )

        self.edit_name = ft.TextField(expand=1, value=self.task.task_name)
        self.edit_view = ft.Row(
            visible=False, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(icon=ft.Icons.DONE_OUTLINE_OUTLINED, icon_color=ft.Colors.GREEN, on_click=self._save_clicked),
            ],
        )
        self.controls = [self.display_view, self.edit_view]

    def _edit_clicked(self, e: ft.ControlEvent) -> None:
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def _save_clicked(self, e: ft.ControlEvent) -> None:
        new_name = self.edit_name.value.strip()
        if new_name:
            self.on_update_name(self.task.id, new_name)
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()
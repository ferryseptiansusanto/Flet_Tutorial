# ---- file: modules/todo/todo_view.py ----
import flet as ft
from modules.todo.todo_components import TodoTaskItem
from modules.todo.todo_logic import TodoLogic

class TodoView(ft.Column):
    def __init__(self, logic: TodoLogic):
        super().__init__(width=600, spacing=25)
        self.logic = logic

        self.new_task_field = ft.TextField(
            hint_text="What needs to be done?", expand=True,
            on_change=lambda e: self.logic.set_new_task_input(e.control.value),
            on_submit=lambda e: self.logic.add_task()
        )

        self.filter_tab_bar = ft.TabBar(
            scrollable=False,
            tabs=[
                ft.Tab(label="all"),
                ft.Tab(label="active"),
                ft.Tab(label="completed"),
            ],
        )

        self.filter_tabs = ft.Tabs(
            length=3,
            selected_index=0,
            on_change=self._on_tab_change,
            content=self.filter_tab_bar,
        )

        self.tasks_container = ft.Column()
        self.controls = [
            ft.Row(controls=[self.new_task_field, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda e: self.logic.add_task())]),
            self.filter_tabs,
            self.tasks_container,
        ]

    def _on_tab_change(self, e: ft.ControlEvent) -> None:
        tab_names = ["all", "active", "completed"]
        status = tab_names[e.control.selected_index]
        self.logic.set_filter(status)

    def render(self) -> None:
        state = self.logic.state
        self.new_task_field.value = state.new_task_input
        self.tasks_container.controls.clear()

        for task in state.tasks:
            is_visible = (state.filter_status == "all") or (state.filter_status == "active" and not task.completed) or (state.filter_status == "completed" and task.completed)
            if is_visible:
                self.tasks_container.controls.append(
                    TodoTaskItem(
                        task=task, 
                        on_status_change=self.logic.toggle_task, 
                        on_update_name=self.logic.update_task_name, 
                        on_delete=self.logic.delete_task
                    )
                )

        # PERBAIKAN: Gunakan try-except untuk mencegah crash saat inisialisasi awal
        try:
            self.update()
        except RuntimeError:
            pass
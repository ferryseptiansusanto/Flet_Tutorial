# ---- file: modules/app_main/app_main_view.py ----
import flet as ft
from typing import Dict
from modules.app_main.app_main_logic import AppMainLogic

class AppMainView(ft.Row):
    def __init__(self, logic: AppMainLogic, module_views: Dict[int, ft.Control]):
        self.logic = logic
        self.module_views = module_views

        self.nav_rail = ft.NavigationRail(
            selected_index=self.logic.state.active_nav_index,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            destinations=[
                ft.NavigationRailDestination(icon=ft.Icons.CALCULATE_OUTLINED, selected_icon=ft.Icons.CALCULATE, label="Kalkulator"),
                ft.NavigationRailDestination(icon=ft.Icons.CHECKLIST_OUTLINED, selected_icon=ft.Icons.CHECKLIST, label="To-Do List"),
            ],
            on_change=lambda e: self.logic.set_nav_index(e.control.selected_index),
        )

        self.content_area = ft.Container(expand=True, padding=30, alignment=ft.Alignment.TOP_CENTER)

        super().__init__(
            expand=True,
            controls=[
                self.nav_rail,
                ft.VerticalDivider(width=1),
                self.content_area,
            ],
        )
        self.render()

    def render(self) -> None:
        self.nav_rail.selected_index = self.logic.state.active_nav_index
        self.content_area.content = self.module_views.get(self.logic.state.active_nav_index)
        # PERBAIKAN: Gunakan try-except
        try:
            self.update()
        except RuntimeError:
            pass
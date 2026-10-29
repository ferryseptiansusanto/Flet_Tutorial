# ---- file: main.py ----
import flet as ft
from core.theme import get_app_theme
from modules.app_main.app_main_coordinator import AppMainCoordinator

def main(page: ft.Page):
    page.title = "Flet 100% Modular"
    page.theme = get_app_theme()
    page.window.width = 900
    page.window.height = 700

    app_root = AppMainCoordinator()
    page.add(app_root.get_view())

if __name__ == "__main__":
    ft.run(main)
# ---- file: modules/calculator/calculator_components.py ----
from typing import Callable
import flet as ft

class CalculatorBaseButton(ft.Button):
    def __init__(self, text: str, on_click_action: Callable[[str], None], expand: int = 1, bgcolor: str = ft.Colors.WHITE_24, color: str = ft.Colors.WHITE):
        super().__init__(
            content=ft.Text(text, size=18, weight=ft.FontWeight.BOLD),
            expand=expand, bgcolor=bgcolor, color=color,
            on_click=lambda _: on_click_action(text),
        )

class CalculatorDigitButton(CalculatorBaseButton):
    def __init__(self, text: str, on_click_action: Callable[[str], None], expand: int = 1):
        super().__init__(text=text, on_click_action=on_click_action, expand=expand, bgcolor=ft.Colors.WHITE_24, color=ft.Colors.WHITE)

class CalculatorActionButton(CalculatorBaseButton):
    def __init__(self, text: str, on_click_action: Callable[[str], None], expand: int = 1):
        super().__init__(text=text, on_click_action=on_click_action, expand=expand, bgcolor=ft.Colors.ORANGE, color=ft.Colors.WHITE)

class CalculatorExtraActionButton(CalculatorBaseButton):
    def __init__(self, text: str, on_click_action: Callable[[str], None], expand: int = 1):
        super().__init__(text=text, on_click_action=on_click_action, expand=expand, bgcolor=ft.Colors.BLUE_GREY_100, color=ft.Colors.BLACK)
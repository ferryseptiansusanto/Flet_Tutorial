# ---- file: modules/calculator/calculator_view.py ----
import flet as ft
from modules.calculator.calculator_components import CalculatorActionButton, CalculatorDigitButton, CalculatorExtraActionButton
from modules.calculator.calculator_logic import CalculatorLogic

class CalculatorView(ft.Container):
    def __init__(self, logic: CalculatorLogic):
        self.logic = logic
        self.display_text = ft.Text(value=self.logic.state.display_value, color=ft.Colors.WHITE, size=28, weight=ft.FontWeight.W_500)
        handle = self.logic.handle_input

        super().__init__(
            width=330, bgcolor=ft.Colors.BLACK, border_radius=ft.BorderRadius.all(20), padding=20,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row(controls=[self.display_text], alignment=ft.MainAxisAlignment.END),
                    ft.Row(controls=[CalculatorExtraActionButton("AC", handle), CalculatorExtraActionButton("+/-", handle), CalculatorExtraActionButton("%", handle), CalculatorActionButton("/", handle)]),
                    ft.Row(controls=[CalculatorDigitButton("7", handle), CalculatorDigitButton("8", handle), CalculatorDigitButton("9", handle), CalculatorActionButton("*", handle)]),
                    ft.Row(controls=[CalculatorDigitButton("4", handle), CalculatorDigitButton("5", handle), CalculatorDigitButton("6", handle), CalculatorActionButton("-", handle)]),
                    ft.Row(controls=[CalculatorDigitButton("1", handle), CalculatorDigitButton("2", handle), CalculatorDigitButton("3", handle), CalculatorActionButton("+", handle)]),
                    ft.Row(controls=[CalculatorDigitButton("0", handle, expand=2), CalculatorDigitButton(".", handle), CalculatorActionButton("=", handle)]),
                ],
            ),
        )

    def render(self) -> None:
        self.display_text.value = self.logic.state.display_value
        # PERBAIKAN: Gunakan try-except
        try:
            self.update()
        except RuntimeError:
            pass
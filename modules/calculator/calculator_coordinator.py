# ---- file: modules/calculator/calculator_coordinator.py ----
import flet as ft
from modules.calculator.calculator_state import CalculatorState
from modules.calculator.calculator_logic import CalculatorLogic
from modules.calculator.calculator_view import CalculatorView

class CalculatorCoordinator:
    def __init__(self):
        self.state = CalculatorState()
        self.logic = CalculatorLogic(state=self.state)
        self.view = CalculatorView(logic=self.logic)
        self.logic.on_change = self.view.render

    def get_view(self) -> ft.Control:
        return self.view
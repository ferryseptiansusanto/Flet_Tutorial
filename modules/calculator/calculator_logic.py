# ---- file: modules/calculator/calculator_logic.py ----
from typing import Callable, Optional
from modules.calculator.calculator_state import CalculatorState

class CalculatorLogic:
    def __init__(self, state: CalculatorState, on_change: Optional[Callable[[], None]] = None):
        self.state = state
        self.on_change = on_change

    def _notify(self) -> None:
        if self.on_change: self.on_change()

    @staticmethod
    def _format_number(num: float) -> str:
        return str(int(num)) if num % 1 == 0 else str(round(num, 8)).rstrip("0").rstrip(".")

    def reset(self) -> None:
        self.state.operator = "+"
        self.state.operand1 = 0.0
        self.state.new_operand = True

    def calculate(self, op1: float, op2: float, operator: str) -> str:
        if operator == "+": return self._format_number(op1 + op2)
        elif operator == "-": return self._format_number(op1 - op2)
        elif operator == "*": return self._format_number(op1 * op2)
        elif operator == "/": return "Error" if op2 == 0 else self._format_number(op1 / op2)
        return str(op2)

    def handle_input(self, data: str) -> None:
        s = self.state
        if s.display_value == "Error" or data == "AC":
            s.display_value = "0"
            self.reset()
        elif data in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."):
            if s.display_value == "0" or s.new_operand:
                s.display_value = data
                s.new_operand = False
            else:
                if not (data == "." and "." in s.display_value):
                    s.display_value += data
        elif data in ("+", "-", "*", "/"):
            curr_val = float(s.display_value) if s.display_value != "Error" else 0.0
            result = self.calculate(s.operand1, curr_val, s.operator)
            s.display_value = result
            s.operator = data
            s.operand1 = 0.0 if result == "Error" else float(result)
            s.new_operand = True
        elif data == "=":
            curr_val = float(s.display_value) if s.display_value != "Error" else 0.0
            s.display_value = self.calculate(s.operand1, curr_val, s.operator)
            self.reset()
        elif data == "%":
            try: s.display_value = self._format_number(float(s.display_value) / 100)
            except ValueError: s.display_value = "Error"
            self.reset()
        elif data == "+/-":
            try:
                if float(s.display_value) != 0: s.display_value = self._format_number(-float(s.display_value))
            except ValueError: s.display_value = "Error"
        
        self._notify()
# ---- file: modules/calculator/calculator_state.py ----
from dataclasses import dataclass

@dataclass
class CalculatorState:
    display_value: str = "0"
    operand1: float = 0.0
    operator: str = "+"
    new_operand: bool = True
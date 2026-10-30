# ---- file: modules/app_main/app_main_coordinator.py ----
import flet as ft
from modules.app_main.app_main_state import AppMainState
from modules.app_main.app_main_logic import AppMainLogic
from modules.app_main.app_main_view import AppMainView
from modules.calculator.calculator_coordinator import CalculatorCoordinator
from modules.todo.todo_coordinator import TodoCoordinator
from modules.chat.chat_coordinator import ChatCoordinator

class AppMainCoordinator:
    def __init__(self):
        # 1. Instansiasi Jembatan Modul Anak
        self.calc_module = CalculatorCoordinator()
        self.todo_module = TodoCoordinator()
        self.chat_module = ChatCoordinator()

        # 2. Setup UDF Internal AppMain
        self.state = AppMainState()
        self.logic = AppMainLogic(state=self.state)

        # 3. Kumpulkan View Anak dan Suntik ke AppMainView
        module_views = {
            0: self.calc_module.get_view(),
            1: self.todo_module.get_view(),
            1: self.chat_module.get_view(),
        }

        self.view = AppMainView(logic=self.logic, module_views=module_views)
        self.logic.on_change = self.view.render

    def get_view(self) -> ft.Control:
        return self.view
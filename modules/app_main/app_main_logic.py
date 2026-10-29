# ---- file: modules/app_main/app_main_logic.py ----
from typing import Callable, Optional
from modules.app_main.app_main_state import AppMainState

class AppMainLogic:
    """Mengelola intent navigasi dari Sidebar."""
    def __init__(self, state: AppMainState, on_change: Optional[Callable[[], None]] = None):
        self.state = state
        self.on_change = on_change

    def set_nav_index(self, index: int) -> None:
        self.state.active_nav_index = index
        if self.on_change:
            self.on_change()
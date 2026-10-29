# ---- file: modules/app_main/app_main_state.py ----
from dataclasses import dataclass

@dataclass
class AppMainState:
    """Status aplikasi utama, seperti index navigasi yang aktif."""
    active_nav_index: int = 0
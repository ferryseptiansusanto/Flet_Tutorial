# ---- file: core/theme.py ----
import flet as ft

def get_app_theme() -> ft.Theme:
    return ft.Theme(
        color_scheme_seed=ft.Colors.BLUE,
        visual_density=ft.VisualDensity.COMPACT
    )
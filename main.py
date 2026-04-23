import flet as ft
from src.controllers.UserController import AuthController
from src.controllers.TareaController import TareaController
from src.views.LoginView import LoginView
from src.views.dashbooard import DashboardView

def main(page: ft.Page):
    page.title = "Sistema SIGE"
    page.window_width = 450
    page.window_height = 700

    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
        else:
            page.views.append(ft.View("/", [ft.Text("Ruta no encontrada")]))

        page.update()

    def view_pop(e):
        page.views.pop()
        if page.views:
            page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/")

ft.app(target=main)
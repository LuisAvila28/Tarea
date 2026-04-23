import flet as ft

class DashboardView(ft.View):
    def __init__(self, page, task_ctrl):
        super().__init__("/dashboard")
        self.page = page
        self.task_ctrl = task_ctrl

        self.controls.append(
            ft.Column([
                ft.Text("Dashboard SIGE", size=24),
                ft.ElevatedButton("Cerrar sesión", on_click=self.logout)
            ], spacing=10, alignment=ft.MainAxisAlignment.CENTER)
        )

    def logout(self, e):
        self.page.go("/")
import flet as ft

class LoginView(ft.View):
    def __init__(self, page, auth_ctrl):
        super().__init__("/login")
        self.page = page
        self.auth_ctrl = auth_ctrl

        self.controls.append(
            ft.Column([
                ft.Text("Bienvenido al Login", size=24),
                ft.TextField(label="Usuario"),
                ft.TextField(label="Contraseña", password=True),
                ft.ElevatedButton("Entrar", on_click=self.login)
            ], spacing=10, alignment=ft.MainAxisAlignment.CENTER)
        )

    def login(self, e):
        # ejemplo simple: ir a dashboard
        self.page.go("/dashboard")
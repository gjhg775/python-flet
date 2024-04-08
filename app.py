import flet as ft
from flet import icons

container = ft.Container(
    ft.Column([
        ft.Container(
            ft.Text(
                "Iniciar sesión",
                width=320,
                size=30,
                text_align="center",
                weight="W900",
                color="white"
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text="Correo electrónico",
                border="underline",
                color="black",
                prefix_icon=ft.icons.EMAIL
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text="Contraseña",
                border="underline",
                color="black",
                prefix_icon=ft.icons.LOCK,
                password=True
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.Checkbox(
                label="Recordar contraseña",
                check_color="black"
            ),
            padding=ft.padding.only(80)
        ),
        ft.Container(
            ft.ElevatedButton(
                text="Iniciar sesión",
                width=280,
                bgcolor="black",
                color="white"
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Text("Iniciar sesión con",
            text_align="center",
            width=320),
        
        ft.Container(
            ft.Row([
                ft.IconButton(
                    icon=ft.icons.EMAIL,
                    tooltip="Google",
                    icon_size=35,
                    icon_color="white"
                ),
                ft.IconButton(
                    icon=ft.icons.FACEBOOK,
                    tooltip="Facebook",
                    icon_size=35,
                    icon_color="white"
                ),
                ft.IconButton(
                    icon=ft.icons.APPLE,
                    tooltip="Apple",
                    icon_size=35,
                    icon_color="white"
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
             padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.Row([
                ft.Text("¿No tiene una cuenta?"),
                ft.TextButton("Crear cuenta")
            ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
            padding=ft.padding.only(20,20)
        )
    ],
    alignment=ft.MainAxisAlignment.SPACE_EVENLY
    ),
    border_radius=20,
    width=320,
    height=500,
    gradient=ft.LinearGradient([
        ft.colors.PURPLE,
        ft.colors.PINK,
        ft.colors.RED
    ])
)

def main(page: ft.Page):
    page.bgcolor=ft.colors.BLACK
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.add(container)

if __name__ == "__main__":
    ft.app(target=main)
    # ft.app(port=9000, target=main, view=ft.AppView.WEB_BROWSER)
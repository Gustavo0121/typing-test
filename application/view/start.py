"""Start."""

import flet as ft

class Start(ft.View):
    """Classe para tela de ínicio."""

    def __init__(self, events: ft.ControlEvent, **kwargs: str):
        """Init for Start class."""
        super().__init__()
        self.events = events
        self.route: str | None = kwargs.get('route')
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.padding = 0
        self.bgcolor = '#181717'
        self.controls=[
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text('Typing test', color='#890606', size=100),
                                offset=ft.Offset(x=0.505, y=0),
                            ),
                            ft.Container(
                                content=ft.Text('Typing test', color='#A40000', size=100),
                                offset=ft.Offset(x=-0.505, y=0),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Text(
                                    'Start', color='#890606',size=100,
                                    ),
                                    offset=ft.Offset(x=0.505, y=0),
                                ),
                                ft.Container(
                                    content=ft.Text(
                                    'Start', color='#A40000',size=100,
                                    ),
                                    offset=ft.Offset(x=-0.505, y=0),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ),
                ],
                spacing=400,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ]
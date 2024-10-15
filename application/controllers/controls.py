"""Componentes."""

import flet as ft
from application import appbar_minus


class AppBar(ft.AppBar):
    """Appbar component."""

    def __init__(self, events: ft.ControlEvent):
        """Init for Appbar class."""
        super().__init__()
        self.events = events
        self.bgcolor = '#181717'
        self.toolbar_height = appbar_minus if self.events.page.window.height < 900 else 100

        self.actions = [
            ft.Container(
                content=ft.IconButton(
                    icon=ft.icons.EXIT_TO_APP,
                    icon_size=70 * self.toolbar_height / 100,
                    icon_color='#A40000',
                    on_click=self.close_app,
                ),
                padding=ft.padding.only(right=15, top=10),
            ),
        ]

    def close_app(self, event: ft.ControlEvent) -> None:
        """Close app."""
        event.page.window_close()

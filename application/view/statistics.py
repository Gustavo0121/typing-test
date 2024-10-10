"""Statistics."""

import flet as ft
from application import seconds, result, phrases, attempts

class Statistics(ft.View):
    """Statistics view."""

    def __init__(self, events: ft.ControlEvent, **kwargs: str):
        """Init for Statistics class."""
        super().__init__()
        self.events = events
        self.route: str | None = kwargs.get('route')
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.padding = 50
        self.bgcolor = '#181717'
        self.controls=[
            ft.Container(
                content=ft.Column(
                    controls=[],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    scroll=ft.ScrollMode.ALWAYS,
                ),
                border=ft.border.all(7, '#640000'),
                height=800,
                width=500,
                bgcolor='#0F0F0F',
            ),
            ft.TextButton(
                content=ft.Text('Next', size=30),
                on_click=self.to_enter,
                style=ft.ButtonStyle(
                    bgcolor='#0F0F0F',
                    color='#640000',
                    shape=ft.BeveledRectangleBorder(radius=10)
                ),
                width=150,
                height=60,
            ),
        ]

        for idx, attempt in enumerate(attempts,start=1):
            controls = self.build_controls(idx, attempt)
            for control in controls:
                self.controls[0].content.controls.append(control)

    def to_enter(self, event: ft.ControlEvent) -> None:
        """To enter."""
        seconds.clear()
        result['erros'] = 0
        result['acertos'] = 0
        phrases.append(phrases[0])
        phrases.pop(0)
        event.page.go('/typing')

    def on_hover(self, event: ft.ControlEvent) -> None:
        """On hover."""
        event.control.bgcolor = (
            '#000000' if event.data == 'true' else '#0F0F0F'
        )
        event.control.update()

    def build_controls(self, idx: int, attempt: list) -> list[ft.Control]:
        """Build the body of controls from view."""
        return [
            ft.Text(f'{str(idx)}º attempt', color='#A40000', size=30),
            ft.Text(f'Tempo total: {attempt[0]} segundos', color='#A40000', size=30),
            ft.Text(f'erros: {attempt[1]}, acertos: {attempt[2]}', color='#A40000', size=30),
            ft.Divider(color='#000000'),
        ]
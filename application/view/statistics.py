"""Statistics."""

import flet as ft
from application import seconds, result, phrases

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
            ft.Text(str(seconds[-1] + 1), color='#A40000', size=100),
            ft.Text(f'erros: {str(result['erros'])}, acertos: {str(result['acertos'])}', color='#A40000', size=100),
            ft.TextButton('Next', on_click=self.to_enter)
        ]

    def to_enter(self, event: ft.ControlEvent) -> None:
        """To enter."""
        seconds.clear()
        result['erros'] = 0
        result['acertos'] = 0
        phrases.append(phrases[0])
        phrases.pop(0)
        event.page.go('/typing')

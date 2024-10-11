"""Typing view."""

from time import sleep

import flet as ft
from application import seconds, result, attempts

class Typing(ft.View):
    """Typing class."""

    def __init__(self, events: ft.ControlEvent, text: str, **kwargs: str):
        """Init for Start class."""
        super().__init__()
        self.events = events
        self.route: str | None = kwargs.get('route')
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.padding = 50
        self.bgcolor = '#181717'
        self.text = text
        self.campo_texto = ft.TextField(
            autofocus=True,
            border=ft.InputBorder.NONE,
            text_size=50,
            multiline=True,
            on_change=self.on_change,
            color='#890606',
            max_lines=1,
        )
        self.controls = [
            ft.Text('0:00', color='#A40000', size=60),
            ft.Stack(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    self.text,
                                    color=ft.colors.with_opacity(
                                        0.3,
                                        '#890606',
                                    ),
                                    size=50,
                                    style=ft.TextStyle(word_spacing=1),
                                ),
                            ],
                        ),
                        padding=ft.padding.all(2),
                    ),
                    ft.Container(
                        content=self.campo_texto,
                        offset=ft.Offset(x=0, y=-0.04),
                    ),
                ],
            ),
        ]

    def on_change(self, event: ft.ControlEvent) -> None:
        """On change."""

        len_field = len(self.campo_texto.value)

        if self.campo_texto.value[-1] == self.text[len_field - 1]:
            result['acertos'] += 1
        else:
            result['erros'] += 1
            list_txt = list(self.campo_texto.value)
            list_txt[-1] = self.text[len_field - 1]
            self.campo_texto.value = ''.join(list_txt)
            self.campo_texto.color = 'white'
            event.page.update()
            sleep(0.2)
            self.campo_texto.color = '#890606'
            event.page.update()

        if len_field == 1:
            sleep(1)
            self.update_counter(event)

        if len_field == len(self.text):
            attempts.append([seconds[-1] + 1, result['erros'], result['acertos']])
            print(f'attempts: {attempts}')
            event.page.go('/statistics')

    def update_counter(self, event:ft.ControlEvent) -> None:
        """Update counter seconds."""
        secs = 0
        while event.page.route == '/typing':
            secs += 1
            self.controls[0].value = f'{secs//60}:{secs%60}'
            event.page.update()
            sleep(1)
            seconds.append(secs)
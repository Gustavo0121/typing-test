"""Typing view."""

from time import sleep

import flet as ft


class Typing(ft.View):
    """Typing class."""

    def __init__(self, events: ft.ControlEvent, **kwargs: str):
        """Init for Start class."""
        super().__init__()
        self.events = events
        self.route: str | None = kwargs.get('route')
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.padding = 50
        self.bgcolor = '#181717'
        self.text = 'You must be the change you wish'
        'to see in the world.'.lower()
        self.campo_texto = ft.TextField(
            autofocus=True,
            border=ft.InputBorder.NONE,
            text_size=60,
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
                                    size=60,
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
            self.campo_texto.color = '#890606'
            print('certo')
        else:
            print('errado')
            list_txt = list(self.campo_texto.value)
            list_txt[-1] = self.text[len_field - 1]
            self.campo_texto.value = ''.join(list_txt)
            self.campo_texto.color = 'white'
            event.page.update()
            sleep(0.5)
            self.campo_texto.color = '#890606'
            event.page.update()

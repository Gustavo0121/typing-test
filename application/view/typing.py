"""Typing view."""

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
        self.text = """
Shall I compare thee to a summer's day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer's lease hath all too short a date;
Sometime too hot the eye of heaven shines,
And often is his gold complexion dimm'd;
And every fair from fair sometime declines,
By chance or nature's changing course untrimm'd;
But thy eternal summer shall not fade,
Nor lose possession of that fair thou ow'st;
Nor shall death brag thou wander'st in his shade,
When in eternal lines to time thou grow'st:
So long as men can breathe or eyes can see,
So long lives this, and this gives life to thee
                            """.lower().strip()
        self.campo_texto = ft.TextField(
            autofocus=True,
            border=ft.InputBorder.NONE,
            text_size=100,
            multiline=True,
            on_change=self.on_change,
            color='#890606',
        )
        self.controls = [
            ft.Stack(
                controls=[
                    ft.Text(
                        self.text,
                        color=ft.colors.with_opacity(0.3, '#890606'),
                        size=100,
                    ),
                    ft.Container(
                        content=self.campo_texto,
                        offset=ft.Offset(x=0, y=-0.05)
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

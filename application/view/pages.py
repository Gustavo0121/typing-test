"""Pages."""

import logging

import flet as ft
from application.view.start import Start
from application.view.typing import Typing
from application.controllers.phrases import phrases


def start_view(e: ft.ControlEvent) -> ft.Control:
    """Start view."""
    logging.debug(e)
    return Start(e, route='/')


def typing_view(e: ft.ControlEvent) -> ft.Control:
    """Typing view."""
    logging.debug(e)
    return Typing(e, route='/typing', text=phrases[0].lower())


def not_found_view(e: ft.ControlEvent) -> ft.Control:
    """Notfount view."""
    logging.debug(e)
    return ft.View(
        route='/notfound',
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        value='Recurso não encontrado...',
                        color='red',
                        weight='bold',
                    ),
                ],
            ),
        ],
    )

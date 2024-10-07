"""Pages."""

import logging

import flet as ft
from pathlib import Path
from application.view.start import Start
from application.view.typing import Typing


def start_view(e: ft.ControlEvent) -> ft.Control:
    """Start view."""
    logging.debug(e)
    return Start(e, route='/')


def typing_view(e: ft.ControlEvent) -> ft.Control:
    """typing view."""
    logging.debug(e)
    return Typing(e, route='/typing')


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

"""Router module."""

import logging
from typing import NoReturn

import flet as ft
from application.view import pages

routes = {
    '/': pages.main_view,
}


def view_pop(e: ft.ControlEvent) -> NoReturn:
    """View pop."""
    logging.info(e)
    e.page.views.pop()
    e.page.go(e.page.views[-1])


def route_change(e: ft.RouteChangeEvent) -> NoReturn:
    """Route change."""
    e.page.views.clear()
    for element in e.page.overlay:
        element.visible = False
    e.page.views.append(routes.get(e.page.route, pages.not_found_view)(e))
    e.page.update()

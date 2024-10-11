"""Main."""

import sys
from pathlib import Path

sys.path.append(
    Path(__file__).parents[1].resolve().as_posix(),
)

import logging
import os

import flet as ft

from application.view.router import route_change, view_pop

if os.getenv('DEBUG_MODE'):
    logging.basicConfig(level=logging.INFO)


def main(page: ft.Page) -> None:
    """Main process."""
    page.title = 'Typing test'
    page.window.min_width = 1280
    page.window.min_height = 720
    page.padding = 0
    page.window.width = page.window.min_width
    page.window.height = page.window.min_height
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window.full_screen = True

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go('/')


def app():
    """Run app."""
    ft.app(target=main, assets_dir='assets')


if __name__ == '__main__':
    app()

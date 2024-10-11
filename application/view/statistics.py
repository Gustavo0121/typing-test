"""Statistics."""

import flet as ft
from application import seconds, result, phrases, attempts, better_utilization, better_temp

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
        self.porcent_better: float = 0
        self.temp_min: float = 0
        self.average: float = 0
        self.controls=[
            ft.Row(
                controls=[
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
                ],
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
            controls_attempt = self.build_controls(idx, attempt)
            for control in controls_attempt:
                self.controls[0].controls[0].content.controls.append(control)

        for idx, attempt in enumerate(attempts,start=1):
            porcent_attempt = (attempt[2] / (attempt[1] + attempt[2])) * 100
            self.average += attempt[0]
            if len(attempts) == 1:
                better_utilization[idx] = attempt
                better_temp[idx] = attempt
                self.temp_min = better_temp[idx][0]
                self.porcent_better = porcent_attempt
                self.average = attempt[0]
                print(f'better_utilization: {better_utilization}')
                print(f'better_temp: {better_temp}')
                controls_podium = self.build_podium()
                for control_podium in controls_podium:
                    self.controls[0].controls[1].content.controls.append(control_podium)
            elif idx == len(attempts):
                self.porcent_better = (better_utilization[list(better_utilization.keys())[-1]][2] / (better_utilization[list(better_utilization.keys())[-1]][1] + better_utilization[list(better_utilization.keys())[-1]][2])) * 100
                self.average = self.average / len(attempts)
                if porcent_attempt >= self.porcent_better:
                    better_utilization[idx] = attempt
                    self.porcent_better = porcent_attempt
                if attempt[0] < better_temp[list(better_temp.keys())[-1]][0]:
                    print(f'segundos: {attempt[0]}')
                    better_temp[idx] = attempt
                    self.temp_min = attempt[0]
                controls_podium = self.build_podium()
                for control_podium in controls_podium:
                    self.controls[0].controls[1].content.controls.append(control_podium)

                print(f'better_utilization: {better_utilization}')
                print(f'better_temp: {better_temp}')

    def to_enter(self, event: ft.ControlEvent) -> None:
        """To enter."""
        seconds.clear()
        result['erros'] = 0
        result['acertos'] = 0
        phrases.append(phrases[0])
        phrases.pop(0)
        self.average = 0
        self.controls[0].controls[1].content.controls.clear()
        event.page.update()
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
            ft.Text(f'{idx}º attempt', color='#A40000', size=30),
            ft.Text(f'Tempo total: {attempt[0]} segundos', color='#A40000', size=30),
            ft.Text(f'erros: {attempt[1]}, acertos: {attempt[2]}', color='#A40000', size=30),
            ft.Divider(color='#000000'),
        ]
    
    def build_podium(self) -> list[ft.Control]:
        """Build the controls of container podium."""
        return [
            ft.Text('Média de tempo gasto'),
            ft.Text(f'Tempo: {self.average:.1f} segundos'),
            ft.Divider(color='#000000'),
            ft.Text('Melhor tempo'),
            ft.Text(f'{list(better_temp.keys())[-1]}º attempt', color='#A40000', size=30),
            ft.Text(f'Tempo total: {better_temp[list(better_temp.keys())[-1]][0]} segundos', color='#A40000', size=30),
            ft.Divider(color='#000000'),
            ft.Text('Melhor porcentagem de acertos'),
            ft.Text(f'{list(better_utilization.keys())[-1]}º attempt', color='#A40000', size=30),
            ft.Text(f'Porcentagem: {self.porcent_better:.1f}%'),
            ft.Divider(color='#000000'),
        ]
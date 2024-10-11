"""Main module."""

import logging
from collections import defaultdict
from pathlib import Path

__title__ = '.'.join(Path(__file__).parent.parts[-2:])

confproject = Path(__file__).parents[1] / 'pyproject.toml'
versionfile = Path(__file__).parent / 'version.txt'
better_temp: defaultdict = defaultdict(lambda: better_temp[1])
better_utilization: defaultdict = defaultdict(lambda: better_utilization[1])
seconds: list = []
result: dict = {
    'erros': 0,
    'acertos': 0,
}
attempts: list = []
phrases: list = [
    'You must be the change you wish to see in the world',
    'Do one thing every day that scares you',
    "In the end, it's not the years in your life that count It's the life in your years",
    'Life is never fair, and perhaps it is a good thing for most of us that it is not',
    'In this life, we cannot do great things We can only do small things with great love',
    "Don't worry when you are not recognized but strive to be worthy of recognition",
    'The greatest glory in living lies not in never falling, but in rising every time we fall',
    "Go confidently in the direction of your dreams Live the life you've imagined",
    'So we beat on, boats against the current, borne back ceaselessly into the past',
    "Keep smiling, because life is a beautiful thing and there's so much to smile about",
]


if __name__ == '__main__':  # pragma: no cover
    logging.info('(%s)', __title__)

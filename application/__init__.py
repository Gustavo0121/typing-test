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
    'With great power comes great responsibility',
    'You must be the change you wish to see in the world',
    'Crying may last a night, but joy comes in the morning',
    'Do one thing every day that scares you',
    'Life is trying things to see if they work',
    'The way to get started is to quit talking and begin doing',
    'It is better to fail in originality than to succeed in imitation',
    'Leave nothing for tomorrow which can be done today',
    'Winning is not everything, but wanting to win is',
    'An unexamined life is not worth living',
]


if __name__ == '__main__':  # pragma: no cover
    logging.info('(%s)', __title__)

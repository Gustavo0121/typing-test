"""Main module."""

import logging
from pathlib import Path

__title__ = '.'.join(Path(__file__).parent.parts[-2:])

confproject = Path(__file__).parents[1] / 'pyproject.toml'
versionfile = Path(__file__).parent / 'version.txt'

if __name__ == '__main__':  # pragma: no cover
    logging.info('(%s)', __title__)

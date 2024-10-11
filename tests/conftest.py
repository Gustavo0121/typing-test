"""Testes de configuração."""

from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest


@pytest.fixture
def temp_file() -> Path:
    """Return temporary file."""
    return Path(NamedTemporaryFile().name)  # noqa: SIM115


@pytest.fixture(scope='session')
def semver_regex() -> str:
    """Fixture para regex de validação do Versionamento Semântico."""
    return r'^\d+(\.\d+){2}((-\w+\.\d+)|(\w+\d+))?$'

"""Módulo de teste do pacote."""

from pathlib import Path
from unittest.mock import patch
import pytest
from importlib import reload
import application as pkg

__author__ = '@Gustavo0121'  # pragma: no cover


@pytest.mark.fast
class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance',
        [
            pkg.confproject,
            pkg.versionfile,
        ],
    )
    def test_exists(self, entrance: Path) -> None:
        """Test if exists files."""
        assert entrance.exists(), f'{entrance=}'

    @pytest.mark.parametrize(
        'entrance',
        [
            pkg.confproject,
            pkg.versionfile,
        ],
    )
    def test_is_file(self, entrance: Path) -> None:
        """Test if are files."""
        assert entrance.is_file(), f'{entrance=}'

    def test_file_not_found(self) -> None:
        """Test FileNotFoundError."""
        with patch(
            'application.Path.open',
            side_effect=FileNotFoundError,
        ):
            try:
                reload(pkg)
            except FileNotFoundError:
                pytest.fail('FileNotFoundError was not handled as expected.')

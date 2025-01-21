"""`pytest configuration"""

import pytest


@pytest.fixture(scope="session")
def serverroot():
    """Return a basic server root."""
    return "http://localhost:8000"

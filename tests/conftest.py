"""`pytest configuration"""

import pytest


@pytest.fixture(scope="session")
def serverroot():
    return "http://localhost:8000"

"""
Conftest module for the calculator.

created on 10.06.2020

@author: Ruslan Dolovanyuk

"""

import os
import sys
sys.path.append(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])

import pytest

from starlette.testclient import TestClient

from main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client

"""
Conftest module for the calculator.

created on 10.06.2020

@author: Ruslan Dolovanyuk

"""

import os
import sys
sys.path.append(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])

import pytest

import mongomock

from starlette.testclient import TestClient

from main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture(autouse=True)
def patch_mongo(monkeypatch):
    db = mongomock.MongoClient()
    def fake_mongo(settings):
        return db
    monkeypatch.setattr('database.get_mongo_client', fake_mongo)

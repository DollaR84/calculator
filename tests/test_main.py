"""
Tests module for the calculator.

created on 10.06.2020

@author: Ruslan Dolovanyuk

"""

from starlette.testclient import TestClient

from main import app


client = TestClient(app)


def test_add(test_app):
    response = client.post("/add", json={"a": 3, "b": 2})
    assert response.status_code == 200
    assert response.json() == {'result': 5.0}


def test_sub(test_app):
    response = client.post("/sub", json={"a": 3, "b": 2})
    assert response.status_code == 200
    assert response.json() == {'result': 1.0}


def test_mul(test_app):
    response = client.post("/mul", json={"a": 3, "b": 2})
    assert response.status_code == 200
    assert response.json() == {'result': 6.0}


def test_div(test_app):
    response = client.post("/div", json={"a": 3, "b": 2})
    assert response.status_code == 200
    assert response.json() == {'result': 1.5}

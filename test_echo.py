import pytest
import requests

API_URL = "https://postman-echo.com/"


@pytest.fixture
def base_url():
    return API_URL


@pytest.fixture
def sample_data():
    return {'name': 'Dilara', 'surname': 'Efremova'}


@pytest.fixture
def session():
    with requests.Session() as sess:
        yield sess


def test_get_empty(base_url, session):
    response = session.get(f"{base_url}get")
    assert response.status_code == 200


def test_get(base_url, session, sample_data):
    response = session.get(f"{base_url}get", params=sample_data)
    assert response.status_code == 200
    assert response.json()['args']['name'] == 'Hello, world!'
    assert response.json()['args']['surname'] == sample_data['surname']


def test_post_json(base_url, session, sample_data):
    response = session.post(f"{base_url}post", json=sample_data)
    assert response.status_code == 200
    assert response.json()['json']['name'] == sample_data['name']
    assert response.json()['json']['surname'] == sample_data['surname']


def test_post_form(base_url, session, sample_data):
    response = session.post(f"{base_url}post", data=sample_data)
    assert response.status_code == 200
    assert response.json()['form']['name'] == sample_data['name']
    assert response.json()['form']['surname'] == sample_data['surname']


def test_delete(base_url, session, sample_data):
    response = session.delete(f"{base_url}delete", params=sample_data)
    assert response.status_code == 200
    assert response.json()['args']['name'] == 'Dilara'
    assert response.json()['args']['surname'] == 'Efremova'
    assert response.json()['json'] is None

import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()


@pytest.mark.xfail(reason="API zwraca 404 dla nieistniejącego posta")
def test_nonexistent_post():
    response = requests.get(f"{BASE_URL}/posts/999999")
    assert response.status_code == 200  # celowo błąd → pipeline będzie czerwony przy xfail

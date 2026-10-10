import pytest
import requests

def test_estado_api():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.status_code == 200

def test_estado_exitoso():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.json()['status'] == 'success'

def test_url_imagen():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.json()['message'].startswith('https://images.dog.ceo/breeds/papillon/n02086910_5488.jpg')

def test_url_pertenece_a_dog_ceo():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert 'images.dog.ceo' in response.json()['message']

#python -m pytest -v qa/tps/test_dog_api.py
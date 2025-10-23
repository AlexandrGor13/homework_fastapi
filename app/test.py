import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

@pytest.fixture(scope='module')
def valid_text_data():
    return {'text': 'Hello'}

@pytest.fixture(scope='module')
def invalid_src_dest_combination():
    return ('invalid', 'lang')

def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to the text translation API'}

def test_translation_valid(valid_text_data):
    data = valid_text_data
    response = client.post('/translation/en-ru', json=data)
    assert response.status_code == 200
    # Предполагаемый вывод после перевода
    assert isinstance(response.json()['text'], str)

def test_translation_invalid_src_dest(invalid_src_dest_combination):
    src, dest = invalid_src_dest_combination
    data = {'text': 'Some text'}
    response = client.post(f'/translation/{src}-{dest}', json=data)
    assert response.status_code == 422  # Unprocessable Entity
    error_message = response.json()
    assert 'detail' in error_message
    assert any("string_pattern_mismatch" in err['type'] for err in error_message['detail'])

def test_translation_same_language(valid_text_data):
    data = valid_text_data
    response = client.post('/translation/en-en', json=data)
    assert response.status_code == 200
    # Так как источник и цель совпадают, ожидается тот же самый текст обратно
    assert response.json() == data
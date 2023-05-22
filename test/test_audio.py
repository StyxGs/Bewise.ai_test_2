from http import HTTPStatus
from os import path, remove
from test.conftest import async_session_marker

from httpx import AsyncClient, Response

from servises.servises import add_user_in_db, give_record
from src.user.models import User


async def test_add_audio(ac: AsyncClient):
    async with async_session_marker() as session:
        new_user: User = await add_user_in_db(username='test', session=session)
    path_dir: str = path.dirname(path.realpath(__file__))
    with open(path_dir + r'\record_test\test.wav', 'rb') as file:
        response: Response = await ac.post('/add-record', files={'file': file},
                                           data={'user_id': new_user.id, 'token': str(new_user.token)})
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'url': 'http://localhost:8000/record?id=1&user_id=1'}


async def test_get_record(ac: AsyncClient):
    path_dir: str = path.dirname(path.realpath(__file__))
    response: Response = await ac.get('/get_record', params={'id': 1, 'user_id': 1})
    async with async_session_marker() as session:
        record_path = await give_record(data={'id': 1, 'user_id': 1}, session=session)
    remove(record_path)
    assert response.status_code == HTTPStatus.OK
    record = response.read()
    with open(path_dir + r'\record_test\test1.mp3', 'wb') as file:
        file.write(record)
    check: bool = path.isfile(path_dir + r'\record_test\test1.mp3')
    remove(path_dir + r'\record_test\test1.mp3')
    assert check

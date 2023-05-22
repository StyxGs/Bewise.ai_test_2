from http import HTTPStatus

from httpx import AsyncClient, Response


async def test_add_user(ac: AsyncClient):
    response: Response = await ac.post('/add-user', json={'username': 'tests'})
    assert response.status_code == HTTPStatus.OK
    assert response.json() is not None

from uuid import UUID
from http import HTTPStatus

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, Header, Form
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.record.schemas import AudioGET
from servises.servises import add_audio_id_db, check_user, give_record
from src.database_contion import get_async_session

router = APIRouter(
    prefix='',
    tags=['record']
)


@router.post('/add-record')
async def add_audio(user_id: int = Form(ge=1), token=Header(),
                    file: UploadFile = File(...),
                    session: AsyncSession = Depends(get_async_session)):
    data_user = {'user_id': user_id, 'token': token}
    user: list = await check_user(user_data=data_user, session=session)
    if user:
        audio_id: int = await add_audio_id_db(file=file, user=data_user, session=session)
        return {'url': f'http://localhost:8000/record?id={audio_id}&user_id={data_user["user_id"]}'}
    else:
        raise HTTPException(detail='Пользователя с такими данными не существует.', status_code=HTTPStatus.UNAUTHORIZED)


@router.get('/get_record')
async def get_record(data: AudioGET = Depends(), session: AsyncSession = Depends(get_async_session)):
    audio_data: str | None = await give_record(data=data.dict(), session=session)
    if audio_data:
        return FileResponse(path=audio_data)
    else:
        raise HTTPException(detail='Аудиозаписи или пользователя с таким id не существует.',
                            status_code=HTTPStatus.UNPROCESSABLE_ENTITY)

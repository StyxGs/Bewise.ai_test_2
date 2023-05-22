from os import path
from uuid import UUID, uuid4

from pydub import AudioSegment
from sqlalchemy import Result, Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.record.models import Record
from src.user.models import User


async def add_user_in_db(username: str, session: AsyncSession):
    new_user = User(username=username)
    session.add(new_user)
    await session.flush()
    await session.commit()
    return new_user


async def check_user(user_data: dict, session: AsyncSession):
    query: Select = select(User).where(User.id == user_data['user_id'], User.token == user_data['token'])
    user = await session.execute(query)
    return user.all()


async def add_audio_id_db(file, user: dict, session: AsyncSession):
    audio = AudioSegment.from_wav(file.file)
    identifier: UUID = uuid4()
    path_dir: str = path.dirname(path.realpath(__file__))
    audio.export(path_dir + fr'\records\{identifier}.mp3', format='mp3')
    new_audio = Record(user_id=user['user_id'],
                       data_audio=path_dir + fr'\records\{identifier}.mp3',
                       identifier_uuid=identifier)
    session.add(new_audio)
    await session.flush()
    await session.commit()
    return new_audio.id


async def give_record(data: dict, session: AsyncSession):
    query: Select = select(Record.data_audio).where(Record.id == data['id'], Record.user_id == data['user_id'])
    result: Result = await session.scalars(query)
    return result.first()

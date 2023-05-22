from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from servises.servises import add_user_in_db
from src.database_contion import get_async_session
from src.user.schemas import UserCreate, UserRead

router = APIRouter(
    prefix='',
    tags=['records']
)


@router.post('/add-user', response_model=UserRead)
async def add_user(user_data: UserCreate, session: AsyncSession = Depends(get_async_session)):
    user = await add_user_in_db(username=user_data.dict()['username'], session=session)
    return user

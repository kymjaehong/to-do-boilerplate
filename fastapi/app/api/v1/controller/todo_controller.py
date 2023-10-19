from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder

from datetime import datetime
from sqlalchemy.sql import func

from dependency_injector.wiring import Provide, inject

from app.core.dependency_container import Container
from app.api.v1.request.todo_request import ToDoCommand
from app.service.todo_service import ToDoService
from app.api.usecase.get_todo_by_user import GetToDoByUserUsecase
from app.api.usecase.register_todo import RegisterToDoUsecase
from app.api.usecase.get_todo_by_cond import GetToDoByCondUsecase

from app.api.api_response import ApiResponse


todo_router = APIRouter(prefix="/todo", tags=["todo"])


@todo_router.get("/{user_id}", response_model=ApiResponse)
@inject
async def get_todo_list(
    user_id: int,
    get_todo_by_user_usecase: GetToDoByUserUsecase = Depends(
        Provide[Container.get_todo_by_user_usecase]
    ),
) -> ApiResponse:
    res = await get_todo_by_user_usecase.execute(user_id=user_id)
    return ApiResponse.ok(data=jsonable_encoder(res))


@todo_router.get("/{user_id}/search", response_model=ApiResponse)
@inject
async def search_todo_list(
    user_id: int,
    keyword: str,
    get_todo_by_cond_usecase: GetToDoByCondUsecase = Depends(
        Provide[Container.get_todo_by_cond_usecase]
    ),
) -> ApiResponse:
    res = await get_todo_by_cond_usecase.execute(user_id=user_id, keyword=keyword)
    return ApiResponse.ok(data=jsonable_encoder(res))


@todo_router.post("/{user_id}", response_model=ApiResponse)
@inject
async def register_todo(
    user_id: int,
    command: ToDoCommand,
    register_todo_usecase: RegisterToDoUsecase = Depends(
        Provide[Container.register_todo_user_usecase]
    ),
) -> ApiResponse:
    created_now = datetime.now()
    res = await register_todo_usecase.execute(
        user_id=user_id, command=command, created_now=created_now
    )
    return ApiResponse.ok(data=jsonable_encoder(res))


@todo_router.patch("/complete/{to_do_id}", response_model=ApiResponse)
@inject
async def update_todo(
    to_do_id: int,
    todo_service: ToDoService = Depends(Provide[Container.todo_service]),
) -> ApiResponse:
    res = await todo_service.update_todo(to_do_id=to_do_id)
    return ApiResponse.ok(data=jsonable_encoder(res))
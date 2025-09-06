from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STaskId, STaskRead

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)

@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
# В Python конструкция после стрелки (-> ...) — это аннотация типа (type hint).
# Она не задаёт значение по умолчанию, а только говорит: «эта функция должна возвращать объект такого типа».
# Здесь -> list[STaskRead] означает: функция вернёт список объектов STaskRead
async def get_tasks() -> list[STaskRead]:
    tasks = await TaskRepository.find_all()
    return tasks

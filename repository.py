from sqlalchemy import select
from backend.database import new_session, TaskOrm
from backend.schemas import STaskAdd, STaskRead

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id 
             
    @classmethod 
    async def find_all(cls) -> list[STaskRead]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STaskRead.model_validate() for task in task_models]
            return task_models
        
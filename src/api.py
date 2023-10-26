from fastapi import APIRouter
from schemas import TaskScheme, TopicScheme
from models.model import Task, Topic
from typing import List
import generators

router = APIRouter()


@router.post("/task/", response_model=Task)
async def create_item(topic: Topic):
    await topic.save()
    task = Task (topic = topic, task = "task", answer = "answer")
    await task.save()
    return task

@router.get("/tasks/", response_model=List[Task])
async def get_items():
    tasks = await Task.objects.all()
    return tasks

@router.post("/task")
async def post_task(topic: TopicScheme):
    problem = generators.GenerateTask(topic)
    #task = Task(Topic(name='topic'), problem='problem')
    return problem
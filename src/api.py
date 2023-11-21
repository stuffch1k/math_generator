from fastapi import APIRouter
from typing import List
from generators import *
from models.topics import *
from models.model import *

router = APIRouter()

# заполнение таблицы topics
# потом вынести в метод при запуске
@router.post("/start", summary="Create topics in db", description="Execute to insert Topics")
async def start_db():
    topic_db =await  Topic.objects.all()
    names = [x.name for x in topic_db]
    for topic in First_Topic.list():
        if topic not in names:
            await Topic.objects.create(name = topic)

@router.get("/tasks/", response_model=List[Task])
async def get_items():
    tasks = await Task.objects.all()
    return tasks

@router.post("/task")
async def create_tasks(tasks: List[TopicWithCompexity]):
    problem = []
    for task in tasks:
        if task.title == "Матрицы":
            for _ in range(task.count):
                problem.append(await GenerateMatrixTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)))
        if task.title == "Определители":
            for _ in range(task.count):
                problem.append(await GenerateDeterminantTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)
                ))
        if task.title == "Обратная матрица":
            for _ in range(task.count):
                problem.append(await GenerateReverseMatrixTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)
                ))
        if task.title == "Ранг":
            for _ in range(task.count):
                problem.append(await GenerateMatrixRankTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)
                ))
    return problem

# @router.get("/test_xml")
# async def get_xml():
#     f = open("src/Test.xml", "r")
#     return f.read()

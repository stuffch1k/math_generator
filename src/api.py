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

@router.get("/topic_task", response_model=List[Task])
async def get_topic_tasks(topic_id:int):
    tasks = await Task.objects.filter(topic=topic_id).all()
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
        if task.title == "Матричные уравнения":
            for _ in range(task.count):
                problem.append(await GenerateMatrixEquationTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)
                ))
        if task.title == "Системы линейных уравнений":
            for _ in range(task.count):
                problem.append(await GenerateLinearEquationTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)
                ))
    return problem

@router.get("/convert_xml")
async def get_xml():
    pass

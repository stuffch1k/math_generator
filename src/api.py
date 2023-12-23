from fastapi import APIRouter, Response
from typing import List
from generators import *
from models.topics import *
from models.model import *
from moodle_export.moodle_converter import *
from models.categories import TEST, category_count
import json

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

@router.post("/import_params")
async def return_query(tasks: List[TopicWithCompexity]):
    return tasks


@router.post("/task")
async def create_tasks(tasks: List[TopicWithCompexity]):
    problem = []
    for task in tasks:
        if task.title == "Матрицы":
            for _ in range(task.count):
                problem.append(await GenerateMatrixTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)))
                category_count["Матрицы"]+=1
        if task.title == "Определители":
            for _ in range(task.count):
                problem.append(await GenerateDeterminantTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)
                ))
                category_count["Определители"]+=1
        if task.title == "Обратная матрица":
            for _ in range(task.count):
                problem.append(await GenerateReverseMatrixTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)
                ))
                category_count["Обратная матрица"]+=1
        if task.title == "Ранг":
            for _ in range(task.count):
                problem.append(await GenerateMatrixRankTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)
                ))
                category_count["Ранг"]+=1
        if task.title == "Матричные уравнения":
            for _ in range(task.count):
                problem.append(await GenerateMatrixEquationTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)
                ))
                category_count["Матричные уравнения"]+=1
        if task.title == "Системы линейных уравнений":
            for _ in range(task.count):
                problem.append(await GenerateLinearEquationTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)
                ))
                category_count["Системы линейных уравнений"]+=1
        if task.title == "Скалярное, векторное, смешанное произведение векторов":
            for _ in range(task.count):
                problem.append(await GenerateVectorTask(
                    TopicForGenerator(title=task.title, complexity=task.complexity)
                ))
                category_count["Скалярное, векторное, смешанное произведение векторов"]+=1
    with open('src/temp_files/test.json', 'w', encoding="utf-8") as file:
        json.dump(problem, file, ensure_ascii=False)
    with open('src/temp_files/categories.json', 'w', encoding="UTF-8") as file:
        json.dump(category_count, file, ensure_ascii=False)
    return problem

@router.get("/convert")
async def converter():
    with open('src/temp_files/test.json', 'r', encoding="utf-8") as file:
        json_test = json.load(file)
    with open('src/temp_files/categories.json','r',  encoding="utf-8") as file:
        json_cats = json.load(file)
    result = convert_to_moodle(json_test, json_cats)
    with open('src/temp_files/test.json', 'wb'):
        pass
    with open('src/temp_files/categories.json', 'wb'):
        pass
    return Response(content = result, media_type="application/xml")



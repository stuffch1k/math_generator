from models.model import *
from schemas import *
import numpy as np
import sympy as sp
import scipy as sc
from random import *
from math import *
from moodle_export.converter import *
from task_generator import *

async def create_db_task(topic_schema, task):
  topic_db = await Topic.objects.get(name = topic_schema.title)
  await Task.objects.create(topic=topic_db.id, 
                            complexity = topic_schema.complexity, 
                            text = str(task["data"]), answer = str(task["answer"])) 


'''
Генерация задач Матрицы
'''
async def GenerateMatrixTask(topic: TopicForGenerator):
    if topic.complexity == 0:
      task = GenerateMatrixSizeTask(topic.title)
      # await create_db_task(topic, task)
      return task
    elif topic.complexity == 1:
      task = GenerateMatrixElementTask(topic.title)
      # await create_db_task(topic, task)
      return task
    elif topic.complexity == 2:
      task = GenerateMatrixSummTask(topic.title)
      # await create_db_task(topic, task)
      return task
    elif topic.complexity == 3:
      task = GenerateMatrixNumberMultiplicationTask(topic.title)
      # await create_db_task(topic, task)
      return task
    elif topic.complexity == 4:
      task = GenerateMatrixTransposeTask(topic.title)
      # await create_db_task(topic, task)
      return task
    elif topic.complexity == 5:
      task = GenerateMatrixMultiplicationTask(topic.title)
      # await create_db_task(topic, task)
      return task


'''
Генерация задач Определители
'''
async def GenerateDeterminantTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
        task = GenerateFindDeterminantTask(topic.title)
        # await create_db_task(topic, task)
        return task
    case 1:
        task = GenerateDeterminantEquationTask(topic.title)
        # await create_db_task(topic, task)
        return task
     

'''
Генерация задач Обратная матрица
'''
async def GenerateReverseMatrixTask(topic: TopicForGenerator):
  match topic.complexity:
     case 0:
        task = GenerateFindReverseMatrixTask(topic.title)
        # await create_db_task(topic, task)
        return task
     case 1:
        task = GenerateFindReversedMatrixElementTask(topic.title)
        # await create_db_task(topic, task)
        return task
     

'''
Генерация задач Ранг
'''
async def GenerateMatrixRankTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateFindMatrixRankTask(topic.title)
      await create_db_task(topic, task)
      return task
    

'''
Генерация задач Матричные уравнения
'''
async def GenerateMatrixEquationTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateSolveMatrixEquationTask(topic.title)
      await create_db_task(topic, task)
      return task
    case 1:
      task = GenerateSolveDoubleMatrixEquationTask(topic.title)
      await create_db_task(topic, task)
      return task


'''
Генерация задач Системы линейных уравнений
'''
async def GenerateLinearEquationTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateSolveLinearEquationTask(topic.title)
      await create_db_task(topic, task)
      return task


'''
Генерация задач Скалярное, векторное, смешанное произведение векторов
'''
async def GenerateVectorTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateScalarVectorMultiplicationTask(topic.title)
      await create_db_task(topic, task)
      return task
    case 1:
      task = GenerateVectorVectorMultiplicationTask(topic.title)
      await create_db_task(topic, task)
      return task
    case 2:
      task = GenerateVectorVectorMultiplicationModuleTask(topic.title)
      await create_db_task(topic, task)
      return task
    case 3:
      task = GenerateMixedVectorMultiplicationTask(topic.title)
      await create_db_task(topic, task)
      return task
    case 4:
      task = GenerateIsCollinearVectorsTask(topic.title)
      await create_db_task(topic, task)
      return task
    case 5:
      task = GenerateIsComplanarVectorsTask(topic.title)
      await create_db_task(topic, task)
      return task


'''
Генерация задач про прямые на плоскости
'''    
async def GenerateLineTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateFindParalelLineEquationTask()
      await create_db_task(topic, task)
      return task
    
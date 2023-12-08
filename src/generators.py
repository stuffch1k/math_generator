from schemas import *
import numpy as np
import sympy as sp
#from models.model import *
from math import *

async def create_db_task(topic_schema, task):
  topic_db = await Topic.objects.get(name = topic_schema.title)
  await Task.objects.create(topic=topic_db.id, 
                            complexity = topic_schema.complexity, 
                            text = str(task["data"]), answer = str(task["answer"])) 

def GenerateMatrixSizeTask():
  matrix = np.random.randint(10, size=(4, 4))
  answer = matrix.shape
  task = "Определите размер матрицы"  #добавить запрос к бд
  dic = {
     "task": task,
     "data": matrix.tolist(),
     "answer": answer}
  return dic


def GenerateMatrixElementTask():
  matrix = np.random.randint(10, size=(4, 4))
  row_count = matrix.shape[0]
  columns_count = matrix.shape[1]
  
  row_index = np.random.randint(0,row_count, size=(1,1))[0][0]
  column_index = np.random.randint(0,columns_count, size=(1,1))[0][0]
  answer = matrix[row_index][column_index]
  task = f'Чему равен элемент матрицы А{row_index, column_index}?' #сделать запрос к бд
  dic = {
    "task": task,
    "data": {
       "matrix":matrix.tolist(),
       "row_index":row_index.item(),
       "column_index":column_index.item()},
    "answer": answer.item()}
  return dic


def GenerateMatrixSummTask():
  first_matrix = np.random.randint(10, size=(3, 3))
  second_matrix = np.random.randint(10, size=(3, 3))
  answer = first_matrix + second_matrix
  task = "Чему равна сумма матриц?" #сделать запрос к бд

  dic = {
     "task": task,
     "data": {"first" : first_matrix.tolist(), "second" : second_matrix.tolist()},
     "answer": answer.tolist()}
  return dic


def GenerateMatrixTransposeTask():
  matrix = np.random.randint(10, size=(3,3))
  answer = matrix.transpose()
  task = "Найдите транспонированную матрицу" #сделать запрос к бд

  dic = {
     "task":task,
     "data": matrix.tolist(),
     "answer": answer.tolist()}
  return dic


def GenerateMatrixNumberMultiplicationTask():
  matrix = np.random.randint(-9, 10, size=(3,3))
  number = np.random.randint(1, 10, size=(1,1))[0][0]
  answer = matrix * number
  task = f"Каков результат умножения числа {number} на матрицу A?" #сделать запрос к бд

  dic = {
    "task":task,
    "data": {"matrix":matrix.tolist(), "number":int(number)},
    "answer": answer.tolist()}
  return dic


def GenerateMatrixMultiplicationTask():
  matrix1 = np.random.randint(-9, 10, size=(3,3))
  matrix2 = np.random.randint(-9, 10, size=(3,3))
  answer = np.dot(matrix1, matrix2)
  task = "Каков результат умножения матриц?" #сделать запрос к бд

  dic = {
    "task":task,
    "data": {"matrix1":matrix1.tolist(), "matrix2":matrix2.tolist()},
    "answer": answer.tolist()}
  return dic


def GenerateFindDeterminantTask():
  matrix = generateNonsingularMatrix(-9, 10, 3, 3)
  answer = np.around(np.linalg.det(matrix))
  task = "Вычислите определитель матрицы А (при необходимости округлите до целого числа)" #Сделать запрос к базе

  dic = {
    "task":task,
    "data": matrix.tolist(),
    "answer": answer}
  return dic


def GenerateDeterminantEquationTask():
  matrix = generateNonsingularMatrix(-9, 10, 3, 3)
  determinant = np.around(np.linalg.det(matrix))

  row_count = matrix.shape[0]
  columns_count = matrix.shape[1]

  row_index = np.random.randint(0,row_count, size=(1,1))[0][0]
  column_index = np.random.randint(0,columns_count, size=(1,1))[0][0]
  random_elem = matrix[row_index][column_index]

  new_matrix = np.where(matrix == random_elem, "x", matrix)
  task = "Какое значение должно стоять на месте x, чтобы соблюдалось равенство?" #Сделать запрос к бд

  dic = {
    "task":task,
    "data": {"matrix": new_matrix.tolist(), "determinant": determinant},
    "answer": int(random_elem)}
  return dic


def GenerateFindReverseMatrixTask():
  matrix = generateNonsingularMatrix(-9, 10, 3, 3)
  answer = np.around(np.linalg.inv(matrix), 3)
  task = "Найдите обратную матрицу (округлить до 3х знаков после запятой)" #Запрос к бд

  dic = {
    "task":task,
    "data": matrix.tolist(),
    "answer": answer.tolist()}
  return dic  


def GenerateFindReversedMatrixElementTask():
  matrix = generateNonsingularMatrix(-9, 10, 3, 3)
  reversed_matrix = np.around(np.linalg.inv(matrix), 3)

  row_count = matrix.shape[0]
  columns_count = matrix.shape[1]  

  row_index = np.random.randint(0,row_count, size=(1,1))[0][0]
  column_index = np.random.randint(0,columns_count, size=(1,1))[0][0]
  random_elem = reversed_matrix[row_index][column_index]
  task = f'Матрица В обратна к исходной матрице. Чему равен элемент матрицы В{row_index, column_index}? Ответ округлите до 3х знаков после запятой.' #Запрос к бд

  dic = {
    "task":task,
    "data": {"matrix": matrix.tolist(), "rowIndex": int(row_index), "columnIndex": int(column_index)},
    "answer": random_elem.item()}
  return dic


def GenerateFindMatrixRankTask():
  switch = np.random.randint(0, 2, size=(1,1))[0][0]
  task = "Определите ранг матрицы" # Сделать запрос к бд

  if switch == 0:
    matrix = np.random.randint(-9, 10, size=(3,3))
    answer = np.linalg.matrix_rank(matrix)
      
  else:
    matrix = np.random.randint(-9, 10, size=(2,3))
    factor1, factor2 = 0, 0
    while factor1 == 0 or factor2 == 0:
        factor1 = np.random.randint(-3, 4, size=(1,1))[0][0]
        factor2 = np.random.randint(-3, 4, size=(1,1))[0][0]

    matrix = np.vstack([matrix, factor1 * matrix[0] + factor2*matrix[1]])
    np.random.shuffle(matrix)
    answer = np.linalg.matrix_rank(matrix)
  
  dic = {
  "task":task,
  "data": matrix.tolist(),
  "answer": answer.item()}
  return dic


def GenerateSolveMatrixEquationTask():
  a = generateNonsingularMatrix(-9, 10, 3, 3)
  b = generateNonsingularMatrix(-9, 10, 3, 3)
  a1 = np.linalg.inv(a)
  answer = np.around(np.dot(a1, b), 3)
  task = "Решите уравнение вида A*X = B. Ответ округлите до 3х знаков после запятой"
  dic = {
  "task":task,
  "data": {"A": a.tolist(), "B": b.tolist()},
  "answer": answer.tolist()}
  return dic


def GenerateSolveDoubleMatrixEquationTask():
  task = "Решите уравнение вида A·X·B = C. Ответ округлите до 3х знаков после запятой"
  a = generateNonsingularMatrix(-9, 10, 3, 3)
  b = generateNonsingularMatrix(-9, 10, 3, 3)
  c = generateNonsingularMatrix(-9, 10, 3, 3)
  a1 = np.linalg.inv(a)
  b1 = np.linalg.inv(b)
  x = np.dot(a1,c)
  answer = np.around(np.dot(x, b1), 3)
  dic = {
  "task":task,
  "data": {"A": a.tolist(), "B": b.tolist(), "C": c.tolist()},
  "answer": answer.tolist()}
  return dic


def GenerateSolveLinearEquationTask():
  a, b, x = generateSLU(3, 3, -5, 20)
  first_equation = f"{a[0][0]}*x + {a[0][1]}*y + {a[0][2]}*z = {b[0].item()}"
  second_equation = f"{a[1][0]}*x + {a[1][1]}*y + {a[1][2]}*z = {b[1].item()}"
  third_equation = f"{a[2][0]}*x + {a[2][1]}*y + {a[2][2]}*z = {b[2].item()}"
  task = "Решите систему линейных уравнений. Ответ округлите до 1го знака после запятой"  
  answer = np.around(x,1).tolist()
  
  moodle_task = f"<p>{task}</p>" + \
  "<p> \\( \\begin{cases}" + \
  f"{a[0][0]}x + {a[0][1]}y + {a[0][2]}z = {b[0].item()} \\\\" + \
  f"{a[1][0]}x + {a[1][1]}y + {a[1][2]}z = {b[1].item()}\\\\" + \
  f"{a[2][0]}x + {a[2][1]}y + {a[2][2]}z = {b[2].item()}" + \
  "\end{cases} \) </p>" + \
  "<p> x={1:NUMERICAL:=" + f'{answer[0][0]}' + ":0.1#OK} </p>" + \
  "<p> y={1:NUMERICAL:=" + f'{answer[1][0]}' + ":0.1#OK} </p>" + \
  "<p> z={1:NUMERICAL:=" + f'{answer[2][0]}' + ":0.1#OK} </p>"
  
  dic = {
  "task":task,
  "moodle_task": moodle_task,
  "data": {"first_equation": first_equation, "second_equation": second_equation, "third_equation" : third_equation},
  "answer": answer}
  return dic


def GenerateScalarVectorMultiplicationTask():
  a = np.random.randint(-20, 21, size=(1,3))
  b = np.random.randint(-20, 21, size=(1,3))
  task = "Вычислите скалярное произведение векторов A и B."
  answer = a * b
  dic = {
    "task": task,
    "data": {"A": a.tolist()[0], "B": b.tolist()[0]},
    "answer": answer.tolist()[0]}
  return dic


def GenerateVectorVectorMultiplicationTask():
  a = np.random.randint(-20, 21, size=(1,3))
  b = np.random.randint(-20, 21, size=(1,3))

  combined = np.vstack([a, b])
  xy = combined[:2, :2]
  yz = combined[:2, 1:3]
  xz = combined[:2, [0, 2]]
  answer = np.array([int(np.linalg.det(yz)), -1 * int(np.linalg.det(xz)), int(np.linalg.det(xy))])
  task = "Вычислите векторное произведение векторов А и В."
  dic = {
    "task": task,
    "data": {"A": a.tolist()[0], "B": b.tolist()[0]},
    "answer": answer.tolist()}
  return dic


def GenerateVectorVectorMultiplicationModuleTask():
  temp = GenerateVectorVectorMultiplicationTask()
  a = temp["data"]["A"]
  b = temp["data"]["B"]
  vector = np.array(temp["answer"])
  answer = np.around(sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2 ), 3)
  task = "Вычислите длинну вектора, полученную в результате векторного произведения A и B"
  dic = {
    "task": task,
    "data": {"A": a.tolist(), "B": b.tolist()},
    "answer": answer.tolist()}
  return dic


def GenerateMixedVectorMultiplicationTask():
  a = np.random.randint(-20, 21, size=(1,3))
  b = np.random.randint(-20, 21, size=(1,3))
  c = np.random.randint(-20, 21, size=(1,3))

  combined = np.vstack([a, b, c])
  answer = np.around(np.linalg.det(combined))
  task = "Вычислите смешанное произведение векторов A, B и C"
  dic = {
    "task": task,
    "data": {"A": a.tolist()[0], "B": b.tolist()[0], "C": c.tolist()[0]},
    "answer": answer}
  return dic

  


def generateSLU(x_count, equation_count, min_value, max_value):
  a = np.random.randint(min_value, max_value, size=(equation_count, x_count))
  while (np.linalg.det(a) == 0):
    a = np.random.randint(min_value, max_value, size=(equation_count, x_count))

  b = np.random.randint(min_value, max_value, size=(x_count, 1))
  x = np.random.randint(1, size=(x_count, 1))

  while((a.dot(x) != b).any()):
    a = np.random.randint(min_value, max_value, size=(equation_count, x_count))
    while (np.linalg.det(a) == 0):
      a = np.random.randint(min_value, max_value, size=(equation_count, x_count))

    b = np.random.randint(min_value, max_value, size=(x_count, 1))
    x = np.linalg.solve(a, b)
  return (a,b,x)


def generateNonsingularMatrix(min_value, max_value, rows_count, columns_count):
  a = np.random.randint(min_value, max_value, size=(rows_count, columns_count))
  while (np.linalg.det(a) == 0):
    a = np.random.randint(min_value, max_value, size=(rows_count, columns_count))

  return a


'''
Генерация задач Матрицы
'''
async def GenerateMatrixTask(topic: TopicForGenerator):
    if topic.complexity == 0:
      task = GenerateMatrixSizeTask()
      await create_db_task(topic, task)
      return task
    elif topic.complexity == 1:
      task = GenerateMatrixElementTask()
      await create_db_task(topic, task)
      return task
    elif topic.complexity == 2:
      task = GenerateMatrixSummTask()
      await create_db_task(topic, task)
      return task
    elif topic.complexity == 3:
      task = GenerateMatrixNumberMultiplicationTask()
      await create_db_task(topic, task)
      return task
    elif topic.complexity == 4:
      task = GenerateMatrixTransposeTask()
      await create_db_task(topic, task)
      return task
    elif topic.complexity == 5:
      task = GenerateMatrixMultiplicationTask()
      await create_db_task(topic, task)
      return task


'''
Генерация задач Определители
'''
async def GenerateDeterminantTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
        task = GenerateFindDeterminantTask()
        await create_db_task(topic, task)
        return task
    case 1:
        task = GenerateDeterminantEquationTask()
        await create_db_task(topic, task)
        return task
     

'''
Генерация задач Обратная матрица
'''
async def GenerateReverseMatrixTask(topic: TopicForGenerator):
  match topic.complexity:
     case 0:
        task = GenerateFindReverseMatrixTask()
        await create_db_task(topic, task)
        return task
     case 1:
        task = GenerateFindReversedMatrixElementTask()
        await create_db_task(topic, task)
        return task
     

'''
Генерация задач Ранг
'''
async def GenerateMatrixRankTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateFindMatrixRankTask()
      await create_db_task(topic, task)
      return task
    

'''
Генерация задач Матричные уравнения
'''
async def GenerateMatrixEquationTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateSolveMatrixEquationTask()
      await create_db_task(topic, task)
      return task
    case 1:
      task = GenerateSolveDoubleMatrixEquationTask()
      await create_db_task(topic, task)
      return task


'''
Генерация задач Системы линейных уравнений
'''
async def GenerateLinearEquationTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateSolveLinearEquationTask()
      await create_db_task(topic, task)
      return task


'''
Генерация задач на действия с векторами
'''
async def GenerateVectorTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateScalarVectorMultiplicationTask()
      await create_db_task(topic, task)
      return task
    case 1:
      task = GenerateVectorVectorMultiplicationTask()
      await create_db_task(topic, task)
      return task
    case 2:
      task = GenerateVectorVectorMultiplicationModuleTask()
      await create_db_task(topic, task)
      return task
    case 3:
      task = GenerateMixedVectorMultiplicationTask()
      await create_db_task(topic, task)
      return task
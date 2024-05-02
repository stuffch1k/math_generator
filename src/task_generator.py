import numpy as np
import sympy as sp
import scipy as sc
from random import *
from math import *
from moodle_export.converter import *
import json

def GenerateMatrixSizeTask(topic):
  matrix = np.random.randint(10, size=(4, 4))
  answer = matrix.shape
  task = "Определите размер матрицы" 
  moodle_task = f"<p>{task}</p>" + \
  f"<p> {create_matrix_ctask(matrix.tolist())}</p>" + \
  "<p> {1:NUMERICAL:=" + f'{answer[0]}' + ":0.0#OK} X {1:NUMERICAL:=" + f'{answer[1]}' + ":0.0#OK} </p>"
  dic = {
    "topic":topic,
     "task": task,
     "data": matrix.tolist(),
     "answer": answer,
    "moodle_task":moodle_task}
  return dic


def GenerateMatrixElementTask(topic):
  matrix = np.random.randint(10, size=(4, 4))
  row_count = matrix.shape[0]
  columns_count = matrix.shape[1]
  
  row_index = np.random.randint(0,row_count, size=(1,1))[0][0]
  column_index = np.random.randint(0,columns_count, size=(1,1))[0][0]
  answer = matrix[row_index][column_index]
  task = f'Чему равен элемент матрицы А{row_index+1, column_index+1}?' #сделать запрос к бд
  moodle_task = f"<p>{task}</p>" + \
  f"<p> {create_matrix_ctask(matrix.tolist())}</p>" + \
  "<p> {1:NUMERICAL:=" + f'{answer.item()}' + ":0.0#OK}</p>"
  dic = {
    "topic":topic,
    "task": task,
    "data": {
       "matrix":matrix.tolist(),
       "row_index":row_index.item(),
       "column_index":column_index.item()},
    "answer": answer.item(),
    "moodle_task": moodle_task}
  return dic


def GenerateMatrixSummTask(topic):
  first_matrix = np.random.randint(10, size=(3, 3))
  second_matrix = np.random.randint(10, size=(3, 3))
  answer = first_matrix + second_matrix
  task = "Чему равна сумма матриц?" #сделать запрос к бд
  moodle_task = f"<p>{task}</p>" + \
  f"<p> {create_matrix_ctask(first_matrix.tolist())} + {create_matrix_ctask(second_matrix.tolist())}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[0])}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[1])}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[2])}</p>" 
  dic = {
    "topic":topic,
     "task": task,
     "data": {"first" : first_matrix.tolist(), "second" : second_matrix.tolist()},
     "answer": answer.tolist(),
     "moodle_task": moodle_task}
  return dic

def GenerateMatrixNumberMultiplicationTask(topic):
  matrix = np.random.randint(-9, 10, size=(3,3))
  number = np.random.randint(1, 10, size=(1,1))[0][0]
  answer = matrix * number
  task = f"Каков результат умножения числа {number} на матрицу?" #сделать запрос к бд
  moodle_task = f"<p>{task}</p>" + \
  f"<p> {create_matrix_ctask(matrix.tolist())} * {number} равно: </p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[0])}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[1])}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[2])}</p>" 
  dic = {
    "topic":topic,
    "task":task,
    "data": {"matrix":matrix.tolist(), "number":int(number)},
    "answer": answer.tolist(),
    "moodle_task":moodle_task}
  return dic

def GenerateMatrixTransposeTask(topic):
  matrix = np.random.randint(10, size=(3,3))
  answer = matrix.transpose()
  task = "Найдите транспонированную матрицу" #сделать запрос к бд
  moodle_task = f"<p>{task}</p>" + \
  f"<p> {create_matrix_ctask(matrix.tolist())}</p>" + \
  f"<p> Транспонированная:</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[0])}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[1])}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[2])}</p>" 
  dic = {
    "topic":topic,
     "task":task,
     "data": matrix.tolist(),
     "answer": answer.tolist(),
     "moodle_task":moodle_task}
  return dic

def GenerateMatrixMultiplicationTask(topic):
  matrix1 = np.random.randint(-9, 10, size=(3,3))
  matrix2 = np.random.randint(-9, 10, size=(3,3))
  answer = np.dot(matrix1, matrix2)
  task = "Каков результат умножения матриц?" #сделать запрос к бд
  moodle_task = f"<p>{task}</p>" + \
  f"<p> {create_matrix_ctask(matrix1.tolist())} * {create_matrix_ctask(matrix2.tolist())}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[0])}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[1])}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[2])}</p>" 
  dic = {
    "topic":topic,
    "task":task,
    "data": {"matrix1":matrix1.tolist(), "matrix2":matrix2.tolist()},
    "answer": answer.tolist(),
    "moodle_task": moodle_task}
  return dic


def GenerateFindDeterminantTask(topic):
  matrix = generateNonsingularMatrix(-9, 10, 3, 3)
  answer = np.around(np.linalg.det(matrix))
  task = "Вычислите определитель матрицы А (при необходимости округлите до целого числа)" #Сделать запрос к базе
  moodle_task = f"<p>{task}</p>" + \
  f"<p> {create_matrix_ctask(matrix.tolist())}</p>" + \
  f"<p> Определитель: {number_convert(int(answer))}</p>"
  dic = {
    "topic":topic,
    "task":task,
    "data": matrix.tolist(),
    "answer": answer, 
    "moodle_task": moodle_task}
  return dic


def GenerateDeterminantEquationTask(topic):
  matrix = generateNonsingularMatrix(-9, 10, 3, 3)
  determinant = np.around(np.linalg.det(matrix))

  row_count = matrix.shape[0]
  columns_count = matrix.shape[1]

  row_index = np.random.randint(0,row_count, size=(1,1))[0][0]
  column_index = np.random.randint(0,columns_count, size=(1,1))[0][0]
  random_elem = matrix[row_index][column_index]

  new_matrix = np.where(matrix == random_elem, "x", matrix)
  task = f"Какое значение должно стоять на месте x, чтобы определитель данной матрицы был равен {determinant}?" #Сделать запрос к бд
  moodle_task = f"<p>{task}</p>" + \
  f"<p> {create_matrix_ctask(new_matrix.tolist())}</p>" + \
  f"<p> X =  {number_convert(int(random_elem))}</p>"
  
  dic = {
    "topic":topic,
    "task":task,
    "data": {"matrix": new_matrix.tolist(), "determinant": determinant},
    "answer": int(random_elem),
    "moodle_task":moodle_task}
  return dic


def GenerateFindReverseMatrixTask(topic):
  matrix = generateNonsingularMatrix(-9, 10, 3, 3)
  answer = np.around(np.linalg.inv(matrix), 1)
  task = "Найдите обратную матрицу (округлить до 3х знаков после запятой)" #Запрос к бд
  moodle_task = f"<p>{task}</p>" + \
  f"<p> {create_matrix_ctask(matrix.tolist())}</p>" + \
  f"<p> Обратная матрица: </p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[0], 3)}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[1], 3)}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[2], 3)}</p>" 

  dic = {
    "topic":topic,
    "task":task,
    "data": matrix.tolist(),
    "answer": answer.tolist(),
    "moodle_task":moodle_task}
  return dic  


def GenerateFindReversedMatrixElementTask(topic):
  matrix = generateNonsingularMatrix(-9, 10, 3, 3)
  reversed_matrix = np.around(np.linalg.inv(matrix), 1)

  row_count = matrix.shape[0]
  columns_count = matrix.shape[1]  

  row_index = np.random.randint(0,row_count, size=(1,1))[0][0]
  column_index = np.random.randint(0,columns_count, size=(1,1))[0][0]
  random_elem = reversed_matrix[row_index][column_index]
  task = f"Найдите элемент {row_index, column_index} матрицы, обратной к данной. Ответ округлите до 3х знаков после запятой."
  # task = f'Матрица В обратна к данной матрице. Чему равен элемент матрицы В{row_index, column_index}? Ответ округлите до 3х знаков после запятой.' #Запрос к бд
  moodle_task = f"<p>{task}</p>" + \
  f"<p>Матрица:</p>" + \
  f"<p>{create_matrix_ctask(matrix.tolist())}</p>" + \
  f"<p>B({row_index, column_index}) = {number_convert(random_elem, 3)}</p>"
  dic = {
    "topic":topic,
    "task":task,
    "data": {"matrix": matrix.tolist(), "rowIndex": int(row_index), "columnIndex": int(column_index)},
    "answer": random_elem.item(),
    "moodle_task" : moodle_task
    }
  return dic


def GenerateFindMatrixRankTask(topic):
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
  
  moodle_task =  f"<p>{task}</p>" + \
  f"<p>{create_matrix_ctask(matrix.tolist())}</p>" + \
  f"<p>Ранг = {number_convert(answer.item())}</p>"
  dic = {
  "topic":topic,
  "task":task,
  "data": matrix.tolist(),
  "answer": answer.item(),
  "moodle_task" : moodle_task
  }
  return dic


def GenerateSolveMatrixEquationTask(topic):
  a = generateNonsingularMatrix(-9, 10, 3, 3)
  b = generateNonsingularMatrix(-9, 10, 3, 3)
  a1 = np.linalg.inv(a)
  answer = np.around(np.dot(a1, b), 1)
  task = "Решите уравнение вида A*X = B. Ответ округлите до 3х знаков после запятой"
  moodle_task = f"<p>{task}</p>" + \
  f"<p>Матрица А = {create_matrix_ctask(a.tolist())}</p>" + \
  f"<p>Матрица В = {create_matrix_ctask(b.tolist())}</p>" + \
  f"<p>Результат: </p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[0], 3)}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[1], 3)}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[2], 3)}</p>"
  dic = {
  "topic":topic,
  "task":task,
  "data": {"A": a.tolist(), "B": b.tolist()},
  "answer": answer.tolist(),
  "moodle_task": moodle_task}
  return dic


def GenerateSolveDoubleMatrixEquationTask(topic):
  task = "Решите уравнение вида A·X·B = C. Ответ округлите до 3х знаков после запятой"
  a = generateNonsingularMatrix(-9, 10, 3, 3)
  b = generateNonsingularMatrix(-9, 10, 3, 3)
  c = generateNonsingularMatrix(-9, 10, 3, 3)
  a1 = np.linalg.inv(a)
  b1 = np.linalg.inv(b)
  x = np.dot(a1,c)
  answer = np.around(np.dot(x, b1), 3)
  moodle_task = f"<p>{task}</p>" + \
  f"<p>Матрица А = {create_matrix_ctask(a.tolist())}</p>" + \
  f"<p>Матрица В = {create_matrix_ctask(b.tolist())}</p>" + \
  f"<p>Матрица C = {create_matrix_ctask(c.tolist())}</p>" + \
  f"<p>Результат: </p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[0], 3)}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[1], 3)}</p>" + \
  f"<p> {matrix_line_convert(answer.tolist()[2], 3)}</p>"
  dic = {
  "topic":topic,
  "task":task,
  "data": {"A": a.tolist(), "B": b.tolist(), "C": c.tolist()},
  "answer": answer.tolist(), 
  "moodle_task": moodle_task}
  return dic


def GenerateSolveLinearEquationTask(topic):
  a, b, x = generateSLU(3, 3, -5, 20)
  first_equation = f"{a[0][0]}*x + {a[0][1]}*y + {a[0][2]}*z = {b[0].item()}"
  second_equation = f"{a[1][0]}*x + {a[1][1]}*y + {a[1][2]}*z = {b[1].item()}"
  third_equation = f"{a[2][0]}*x + {a[2][1]}*y + {a[2][2]}*z = {b[2].item()}"
  task = "Решите систему линейных уравнений. Ответ округлите до 3х знаков после запятой"  
  answer = np.around(x,3).tolist()
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
  "topic":topic,
  "task":task,
  "data": {"first_equation": first_equation, "second_equation": second_equation, "third_equation" : third_equation},
  "answer": answer,
  "moodle_task":moodle_task}
  return dic


def GenerateScalarVectorMultiplicationTask(topic):
  a = np.random.randint(-20, 21, size=(1,3))[0]
  b = np.random.randint(-20, 21, size=(1,3))[0]
  task = f"Вычислите скалярное произведение векторов {vector_name_convert('a')} и {vector_name_convert('b')}."
  answer = a @ b
  moodle_task = f"<p>{task}</p>" + \
  f"<p>{vector_convert('a', a.tolist())}</p>" + \
  f"<p>{vector_convert('b', b.tolist())}</p>" + \
  f"<p>{vector_scalar_convert(answer.item())}</p>"
  dic = {
    "topic":topic,
    "task": task,
    "data": {"A": a.tolist(), "B": b.tolist()},
    "answer": answer.item(),
    "moodle_task": moodle_task}
  return dic


def GenerateVectorVectorMultiplicationTask(topic):
  a = np.random.randint(-20, 21, size=(1,3))
  b = np.random.randint(-20, 21, size=(1,3))

  answer = np.cross(a,b)[0].tolist()
  task = f"Вычислите векторное произведение векторов {vector_name_convert('a')} и {vector_name_convert('b')}."
  moodle_task = f"<p>{task}</p>" + \
  f"<p>{vector_convert('a', a.tolist()[0])}</p>" + \
  f"<p>{vector_convert('b', b.tolist()[0])}</p>" + \
  f"<p>{vector_vector_convert(answer)}</p>"
  dic = {
    "topic":topic,
    "task": task,
    "data": {"A": a.tolist()[0], "B": b.tolist()[0]},
    "answer": answer,
    "moodle_task":moodle_task}
  return dic


def GenerateVectorVectorMultiplicationModuleTask(topic):
  temp = GenerateVectorVectorMultiplicationTask(topic)
  a = temp["data"]["A"]
  b = temp["data"]["B"]
  vector = np.array(temp["answer"])
  answer = np.around(sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2 ), 1)
  task = f"Вычислите длину вектора {vector_name_convert('c')}, полученную в результате векторного произведения  {vector_name_convert('a')} и {vector_name_convert('b')}. Ответ округлите до 1 знака после запятой."
  moodle_task = f"<p>{task}</p>" + \
  f"<p>{vector_convert('a', a)}</p>" + \
  f"<p>{vector_convert('b', b)}</p>" + \
  f"<p>{vector_module('c', answer.item())}</p>"
  dic = {
    "topic":topic,
    "task": task,
    "data": {"A": a, "B": b},
    "answer": answer.tolist(),
    "moodle_task":moodle_task}
  return dic


def GenerateMixedVectorMultiplicationTask(topic):
  a = np.random.randint(-20, 21, size=(1,3))
  b = np.random.randint(-20, 21, size=(1,3))
  c = np.random.randint(-20, 21, size=(1,3))

  combined = np.vstack([a, b, c])
  answer = np.around(np.linalg.det(combined))
  task = f"Вычислите смешанное произведение векторов {vector_name_convert('a')}, {vector_name_convert('b')} и {vector_name_convert('c')}."
  moodle_task = f"<p>{task}</p>" + \
  f"<p>{vector_convert('a', a.tolist()[0])}</p>" + \
  f"<p>{vector_convert('b', b.tolist()[0])}</p>" + \
  f"<p>{vector_convert('c', c.tolist()[0])}</p>" + \
  f"<p>{mixed_mult(int(answer))}</p>"
  dic = {
    "topic":topic,
    "task": task,
    "data": {"A": a.tolist()[0], "B": b.tolist()[0], "C": c.tolist()[0]},
    "answer": answer,
    "moodle_task": moodle_task}
  return dic


def GenerateIsCollinearVectorsTask(topic):
  switch = np.random.randint(0, 2, size=(1,1))[0][0]

  if switch == 0:
    a = np.random.randint(-20, 21, size=(1,3))[0]
    b = np.random.randint(-20, 21, size=(1,3))[0]
  else:
    fraction = np.random.randint(-3, 5, size=(1,1))[0][0]
    a = np.random.randint(-20, 21, size=(1,3))[0]
    b = fraction * a

  first,second,third = a[0]/b[0],a[1]/b[1],a[2]/b[2]

  task = "Являются ли два приведенных ниже вектора коллинеарными? В ответе указать Да или Нет."
  answer = "Да" if np.equal(first,second) and np.equal(first,third) else "Нет"
  moodle_task = f"<p>{task}</p>" + \
  f"<p>{vector_convert('a', a.tolist())}</p>" + \
  f"<p>{vector_convert('b', b.tolist())}</p>" + \
  f"<p>{true_false_cloze(answer)}</p>" 
  dic = {
    "topic":topic,
    "task": task,
    "data": {"A": a.tolist(), "B": b.tolist()},
    "answer": answer,
    "moodle_task":moodle_task}
  return dic


def GenerateIsComplanarVectorsTask(topic):
  switch = np.random.randint(0, 2, size=(1,1))[0][0]

  if switch == 0:
    data = generateNonsingularMatrix(-20, 21, 3, 3)
  else:
    data = generateSingularMatrix(-20, 21, 3, 3)
  
  task = "Являются ли три приведенных ниже вектора компланарными? В ответе указать Да или Нет."
  answer = "Да" if switch != 0 else "Нет"
  moodle_task = f"<p>{task}</p>" + \
  f"<p>{vector_convert('a', data[0].tolist())}</p>" + \
  f"<p>{vector_convert('b', data[1].tolist())}</p>" + \
  f"<p>{vector_convert('c', data[2].tolist())}</p>" + \
  f"<p>{true_false_cloze(answer)}</p>"
  dic = {
    "topic":topic,
    "task": task,
    "data": {"A": data[0].tolist(), "B":data[1].tolist(), "C": data[2].tolist()},
    "answer": answer,
    "moodle_task":moodle_task}
  
  return dic


def GenerateFindLineEquationByPointsTask(topic):
  A1,A2 = randint(-9, 9),randint(-9, 9)
  B1,B2 = randint(-9, 9),randint(-9, 9)

  A, B = sp.Point(A1, A2), sp.Point(B1, B2)
  L = sp.Line(A, B)

  task = f"Составить уравнение прямой, проходящей через две точки:  A({A1},{A2})  и  B({B1},{B2})"
  answer = L.equation()
  moodle_task = f"<p>{task}</p>" + \
  f"<p>Уравнение: {convert_equation(answer.args)}</p>"
  dic = {
  "topic": topic,
  "task": task,
  "data": {}, #Нужно ли тут что - то на фронт возвращать? все данные уже в задаче.
  "answer": str(answer),
  "moodle_task": moodle_task}
  return dic


def GenerateFindParalelLineEquationByEquationTask(topic):
  A1,A2 = randint(-9, 9),randint(-9, 9)
  A = sp.Point(A1,A2)
  B1,B2 = randint(-9, 9),randint(-9, 9)
  L1 = sp.Line((0, 0), (B1, B2))

  L2 = L1.parallel_line(A)
  task = f"Известно, что прямая  L  проходит через начало координат и точку  B({B1},{B2}). Записать уравнение прямой, проходящей через точку  A({A1},{A2})  параллельно прямой  L"
  answer = L2.equation()
  moodle_task = f"<p>{task}</p>" + \
  f"<p>Уравнение: {convert_equation(answer.args)}</p>"
  dic = {
    "topic":topic,
    "task": task,
    "data": {}, #Нужно ли тут что - то на фронт возвращать? все данные уже в таске.
    "answer": str(answer),
    "moodle_task": moodle_task}
  
  return dic


def GenerateFindParalelLineEquationByPointsTask(topic):
  A1,A2 = randint(-9, 9),randint(-9, 9)
  B1,B2 = randint(-9, 9),randint(-9, 9)
  C1,C2 = randint(-9, 9),randint(-9, 9)
  A = sp.Point(A1,A2)
  L1 = sp.Line((B1, B2), (C1, C2))

  L2 = L1.parallel_line(A)
  task = f"Составить уравнение прямой, проходящей через точку А({A1},{A2}), параллельную прямой BC, если B({B1},{B2}), C({C1},{C2})"
  answer = L2.equation()
  moodle_task = f"<p>{task}</p>" + \
  f"<p>Уравнение: {convert_equation(answer.args)}</p>"
  dic = {
  "topic":topic,
  "task": task,
  "data": {}, #Нужно ли тут что - то на фронт возвращать? все данные уже в задаче.
  "answer": str(answer),
  "moodle_task": moodle_task}
  return dic


def GenerateFindCrossPointOfTwoLinesTask(topic):
  A1,A2 = randint(-9, 9),randint(-9, 9)
  B1,B2 = randint(-9, 9),randint(-9, 9)
  C1,C2 = randint(-9, 9),randint(-9, 9)
  D1,D2 = randint(-9, 9),randint(-9, 9)

  L1 = sp.Line((A1, A2), (B1, B2))
  L2 = sp.Line((C1, C2), (D1, D2))

  task = f"Найти точку пересечения прямых L1 и L2, если известно, что прямая L1 проходит через точки А({A1},{A2}) и B({B1},{B2}), а прямая L2 проходит через точки C({C1},{C2}) и D({D1},{D2})"
  answer = L1.intersection(L2)[0].coordinates
  moodle_task=f"<p>{task}</p>" + \
  f"<p>Точка пересечения: ({sqrt_view_answer(answer[0])}, {sqrt_view_answer(answer[1])})</p>"
  dic = {
  "topic":topic,
  "task": task,
  "data": {}, #Нужно ли тут что - то на фронт возвращать? все данные уже в задаче.
  "answer": str(answer),
  "moodle_task": moodle_task 
 } 

  return dic


def GenerateFindDicstanceFromLineToPointTask(topic):
  A1,A2 = randint(-9, 9),randint(-9, 9)
  B1,B2 = randint(-9, 9),randint(-9, 9)
  C1,C2 = randint(-9, 9),randint(-9, 9)

  C = sp.Point(C1, C2)
  L1 = sp.Line((A1, A2), (B1, B2))

  task = f"Известно, что прямая L проходит через точки A({A1},{A2}) и B({B1},{B2}). Из точки C({C1},{C2}) на прямую L опущен перпендикуляр, который касается её в точке D. Определить длину отрезка CD. Пример формы ответа: 3*sqrt(26)/13"
  answer = L1.perpendicular_segment(C).length
  moodle_task=f"<p>{task}</p>" + \
  f"<p>Ответ: \( {sqrt_view_answer(answer)} \)</p>"
  dic = {
  "topic":topic,
  "task": task,
  "data": {}, #Нужно ли тут что - то на фронт возвращать? все данные уже в задаче.
  "answer": str(answer),
  "moodle_task":moodle_task}
  return dic


def GenerateFindPlaneEquationByThreePointsTask(topic):
  A1,A2,A3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)
  B1,B2,B3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)
  C1,C2,C3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)

  alpha = sp.Plane(sp.Point3D(A1, A2, A3), sp.Point3D(B1, B2, B3), sp.Point3D(C1, C2, C3))

  task = f"Записать уравнение плоскости, проходящей через точки A({A1},{A2},{A3}), B({B1},{B2},{B3}), C({C1},{C2},{C3}). Пример формы записи ответа: 38*x - 136*y - 126*z - 574"
  answer = alpha.equation()

  moodle_task=f"<p>{task}</p>" + \
  f"<p>Уравнение: {convert_plane_equation(answer.args)}</p>"

  dic = {
  "topic": topic,
  "task": task,
  "data": {}, #Нужно ли тут что - то на фронт возвращать? все данные уже в задаче.
  "answer": str(answer),
  "moodle_task":moodle_task}
  return dic


def GenerateFindPlaneEquationByPointAndNormalVector(topic):
  A1,A2,A3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)
  B1,B2,B3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)

  alpha = sp.Plane(sp.Point3D(A1, A2, A3), normal_vector =(B1, B2, B3))

  task = f"Записать уравнение плоскости a, которая проходит через точку M({A1},{A2},{A3}) и перпендикулярна вектору n =({B1},{B2},{B3}). Пример записи ответа: -3*x - 8*y - 8*z + 85"
  answer = alpha.equation()

  moodle_task=f"<p>{task}</p>" + \
  f"<p>Уравнение: {convert_plane_equation(answer.args)}</p>"
  dic = {
  "topic": topic,
  "task": task,
  "data": {}, #Нужно ли тут что - то на фронт возвращать? все данные уже в задаче.
  "answer": str(answer),
  "moodle_task": moodle_task}
  return dic


def GenerateFindParallelPlaneEquationTask(topic):
  A1,A2,A3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)
  B1,B2,B3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)
  P1,P2,P3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)

  task = f"Плоскость α проходит через точку M({A1},{A2},{A3}) и перепендикулярна вектору n =({B1},{B2},{B3}). Найти уравнение плоскости β, параллельной α и проходящей через точку P({P1},{P2},{P3})"
  
  alpha = sp.Plane(sp.Point3D(A1, A2, A3), normal_vector =(B1, B2, B3))

  parallelPlane = alpha.parallel_plane(sp.Point3D(P1,P2,P3))
  answer = parallelPlane.equation()

  moodle_task=f"<p>{task}</p>" + \
  f"<p>Уравнение: {convert_plane_equation(answer.args)}</p>"

  dic = {
    "topic":topic,
    "task": task,
    "data": {}, #Нужно ли тут что - то на фронт возвращать? все данные уже в задаче.
    "answer": str(answer),
    "moodle_task":moodle_task}
  
  return dic


def GenerateFindOrtPlaneEquationTask(topic):
  A1,A2,A3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)
  B1,B2,B3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)
  P1,P2,P3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)
  N1,N2,N3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)

  task = f"Плоскость α имеет нормальный вектор n =({N1},{N2},{N3}) и проходит через точку P({P1},{P2},{P3}). Найти уравнение плоскости, перпендикулярной α и проходящей через точки A({A1},{A2},{A3}) и B({B1},{B2},{B3}))"

  alpha = sp.Plane(sp.Point3D(P1, P2, P3), normal_vector =(N1, N2, N3))
  A,B = sp.Point3D(A1,A2,A3), sp.Point3D(B1,B2,B3)

  ortPlane = alpha.perpendicular_plane(A,B)
  answer = ortPlane.equation()
  moodle_task=f"<p>{task}</p>" + \
  f"<p>Уравнение: {convert_plane_equation(answer.args)}</p>"

  dic = {
  "topic":topic,
  "task": task,
  "data": {}, #Нужно ли тут что - то на фронт возвращать? все данные уже в задаче.
  "answer": str(answer),
  "moodle_task": moodle_task}
  return dic


def GeneratePointProjectionOnLineTask(topic):
  A1,A2,A3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)
  N1,N2,N3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)
  M1,M2,M3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)

  task = f"Известно, что прямая L проходит через точку N({N1},{N2},{N3}) и точку M({M1},{M2},{M3}). Найти координаты проекции точки A({A1},{A2},{A3}) на прямую L"

  A = sp.Point(A1,A2,A3)
  line = sp.Line((N1,N2,N3),(M1,M2,M3))
  answer = line.projection(A).coordinates

  moodle_task=f"<p>{task}</p>" + \
  f"<p>Координаты: {rational_plane(answer)}</p>"
  dic = {
  "topic":topic,  
  "task": task,
  "data": {}, 
  "answer": str(answer),
  "moodle_task":moodle_task}
  return dic


def GeneratePointProjectionOnPlainTask(topic):
  A1,A2,A3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)
  N1,N2,N3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)
  P1,P2,P3 = randint(-9, 9),randint(-9, 9),randint(-9, 9)

  task = f"Известно, что плоскость α проходит через точку P({P1},{P2},{P3})  и перпендикулярна вектору n =({N1},{N2},{N3}). Найти координаты проекции точки A({A1},{A2},{A3}) на плоскость α"
  
  A = sp.Point(A1, A2, A3)

  alpha = sp.Plane(sp.Point3D(P1, P2, P3), normal_vector =(N1, N2, N3))
  answer = alpha.projection(A).coordinates
  
  moodle_task=f"<p>{task}</p>" + \
  f"<p>Координаты: {rational_plane(answer)}</p>"
  dic = {
  "topic":topic,  
  "task": task,
  "data": {}, 
  "answer": str(answer),
  "moodle_task":moodle_task}
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


def generateSingularMatrix(min_value, max_value, rows_count, columns_count):
  a = np.random.randint(min_value, max_value, size=(rows_count, columns_count))
  while (np.linalg.det(a) != 0):
    a = np.random.randint(min_value, max_value, size=(rows_count, columns_count))
  return a

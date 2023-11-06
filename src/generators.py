from schemas import *
import numpy as np
import sympy as sp

def GeterateMatrixSizeTask():
  matrix = np.random.randint(10, size=(4, 4))
  answer = matrix.shape
  task = ""  #добавить запрос к бд
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
  task = '' #сделать запрос к бд

  dic = {
    "task": task,
    "data": {
       "matrix":matrix.tolist(),
       "row_index":row_index,
       "column_index":column_index},
    "answer": answer}
  return dic


def GenerateMatrixSummTask():
  first_matrix = np.random.randint(10, size=(3, 3))
  second_matrix = np.random.randint(10, size=(3, 3))
  answer = first_matrix + second_matrix
  task = "" #сделать запрос к бд

  dic = {
     "task": task,
     "data": {"first" : first_matrix.tolist(), "second" : second_matrix.tolist()},
     "answer": answer}
  return dic


def GenerateMatrixTransposeTask():
  matrix = np.random.randint(10, size=(3,3))
  answer = matrix.transpose()
  task = "" #сделать запрос к бд

  dic = {
     "task":task,
     "data": matrix.tolist(),
     "answer": answer.tolist()}
  return dic


def GenerateMatrixNumberMultiplicationTask():
  matrix = np.random.randint(-9, 10, size=(3,3))
  number = np.random.randint(1, 10, size=(1,1))[0][0]
  answer = matrix * number
  task = "" #сделать запрос к бд

  dic = {
    "task":task,
    "data": {"matrix":matrix.tolist(), "number":number},
    "answer": answer.tolist()}
  return dic


def GenerateMatrixMultiplicationTask():
  matrix1 = np.random.randint(-9, 10, size=(3,3))
  matrix2 = np.random.randint(-9, 10, size=(3,3))
  answer = np.dot(matrix1, matrix2)
  task = "" #сделать запрос к бд

  dic = {
    "task":task,
    "data": {"matrix1":matrix1.tolist(), "matrix2":matrix2.tolist()},
    "answer": answer.tolist()}
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


def generateNonsingularMatrix(rows_count, columns_count, min_value, max_value):
  a = np.random.randint(min_value, max_value, size=(rows_count, columns_count))
  while (np.linalg.det(a) == 0):
    a = np.random.randint(min_value, max_value, size=(rows_count, columns_count))

  return a


def GenerateMatrixTask(topic: TopicScheme):
    if topic.title == 0:
        return GeterateMatrixSizeTask()
    elif topic.title == 1:
        return GenerateMatrixElementTask()
    elif topic.title == 2:
        return Exception()
    elif topic.title == 3:
       return GenerateMatrixSummTask()
    elif topic.title == 4:
       return GenerateMatrixNumberMultiplicationTask()
    elif topic.title == 6:
       return GenerateMatrixTransposeTask()
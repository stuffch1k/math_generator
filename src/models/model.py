import databases
import sqlalchemy
from typing import Optional, Union, Dict
import ormar
import sys
import os
sys.path.append(os.path.join(sys.path[0], 'src'))
from database import database, metadata


class Topic(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
    id: int = ormar.Integer(primary_key = True)
    name: str = ormar.Text()

class Text(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
    id: int = ormar.Integer(primary_key = True)
    topic: Optional[Topic] = ormar.ForeignKey(Topic)
    complexity: int = ormar.Integer()
    text: str = ormar.Text()

class Task(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
    id: int = ormar.Integer(primary_key = True)
    topic: Optional[Topic] = ormar.ForeignKey(Topic)
    complexity: float = ormar.Float()
    text: str = ormar.Text()
    answer: str = ormar.Text()

''' 
Матрицы 10 средняя
Метод Крамера 5 сложные


0-9
10-20 средняя
21-30

сумма матриц - 7
3х3 - 3
округление - 2

формулировка задачи + размеры данных + окргуление
'''

# Замените элемент {element} на такой, чтобы детерминант был равен {determinant}


  


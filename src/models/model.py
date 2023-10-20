import databases
import sqlalchemy
from typing import Optional, Union, Dict
import ormar
from database import DATABASE_URL

metadata = sqlalchemy.MetaData()

database = databases.Database(DATABASE_URL)

class Element(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
    id: int = ormar.Integer(primary_key = True)
    name: str = ormar.Text()
    
class Topic(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
    id: int = ormar.Integer(primary_key = True)
    name: str = ormar.Text()
    element: Optional[Union[Element, Dict]] = ormar.ForeignKey(Element, nullable = True)

class Task(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
    id: int = ormar.Integer(primary_key = True)
    topic: Optional[Union[Topic, Dict]] = ormar.ForeignKey(Topic)
    task: str = ormar.Text()
    answer: str = ormar.Text()

    


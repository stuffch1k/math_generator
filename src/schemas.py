from pydantic import BaseModel
from typing import Optional, Any
from uuid import UUID
from models.topics import *

class TopicWithCompexity(BaseModel):
    title: First_Topic
    complexity: int
    count: int = 1
    class Config:  
        use_enum_values = True

class TopicForGenerator(BaseModel):
    title: First_Topic
    complexity: int 

class UUIDGenerator(BaseModel):
    uuid: UUID
    count: int = 1
    topic: First_Topic = None

class Answer(BaseModel): #небезопасно, убрать экстру когда соединим фронт
    topic: First_Topic
    moodle_task: str
    class Config:
        extra = "allow"

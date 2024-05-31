from pydantic import BaseModel
from typing import Optional, Any, Union
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
    topic: Union[First_Topic, str] = None

class Answer(BaseModel): 
    topic: Union[First_Topic, str]
    moodle_task: str

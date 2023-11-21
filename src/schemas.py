from pydantic import BaseModel
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
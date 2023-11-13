from pydantic import BaseModel
from enum import Enum

class Subtitle(Enum):
    matrix = 0
    find_determinant = 1
    Gauss_method = 2

class TopicScheme(BaseModel):
    title : Subtitle

    class Config:  
        use_enum_values = True

class TaskScheme(BaseModel):
    description: str
    task: str


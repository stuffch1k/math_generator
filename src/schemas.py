from pydantic import BaseModel
from enum import Enum

class Title(Enum):
    Matrix = 0
    Linear_algebra = 1

class Subtitle(Enum):
    find_determinator = 0
    Gauss_method = 1

class TopicScheme(BaseModel):
    title : Title
    subtitle : Subtitle

    class Config:  
        use_enum_values = True

class TaskScheme(BaseModel):
    description: str
    task: str


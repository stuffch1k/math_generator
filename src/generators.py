from schemas import *
import numpy as np
import sympy as sp

def GenerateMatrixTask(topic: TopicScheme):
    if topic.subtitle == 0:
        matrix = np.random.randint(10, size=(4, 4))
        dic = {"data": matrix.tolist()}
        return dic



def GenerateTask(topic: TopicScheme):
    if topic.title == 0:
        return GenerateMatrixTask(topic)
    elif topic.title == 1:
        return Exception()
        #GenerateLinAlTask(topic)
    else:
        return Exception()
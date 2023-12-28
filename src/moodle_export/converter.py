from schemas import TopicWithCompexity
import xml.etree.ElementTree as ET
import re

def create_matrix_ctask(matrix):
    result = f""
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            result+=str(matrix[i][j])
            if j == len(matrix) - 1 and i!=len(matrix)-1:
                result+=r"\\"
            else:
                result+=r" & "
    begin = r"\( \begin{pmatrix}"
    end = r"\end{pmatrix} \)"
    return begin+result+end

def number_convert(answer, round = 0):
    return f"{{1:NUMERICAL:={answer}:0.{round}#OK}}"

def matrix_line_convert(line, round = 0):
    cline = ""
    for i in range(len(line)):
        cline+=f"{{1:NUMERICAL:={line[i]}:0.{round}#OK}}"
        if i != len(line) - 1:
            cline+=", "
    return cline

def vector_name_convert(vector_name):
    begin = r"\( \vec{"
    end = r"} \)"
    return begin+vector_name+end

def vector_convert(vector_name, vector):
    begin = r"\( \vec{"
    end = r" \)"
    vec_name = vector_name
    vector_nums = f"{vector[0], vector[1], vector[2]}"
    result = begin+vec_name+r"} = " + vector_nums + end
    return result

def vector_scalar_convert(answer):
    result = number_convert(answer)
    return r"\( \vec{a} \cdot \vec{b} = \)" + result

def vector_vector_convert(answer):
    result = matrix_line_convert(answer)
    return r"\( \vec{a} \times \vec{b} = \)" + result

def vector_module(vector_name, answer):
    begin = r"\( |\vec{"
    return begin + vector_name + r"}| = \)" + number_convert(answer, 1)

def mixed_mult(answer):
    result = number_convert(answer)
    return r"\( \vec{a} \cdot (\vec{b} \times \vec{c}) = \)" + result

def true_false_cloze(answer):
    yes = 0
    no = 0
    if answer == "Да":
        yes = 100
    else: 
        no = 100
    return f"{{1:SHORTANSWER:%{yes}%Да#~%{no}%Нет#}}"

def convert_equation(args):
    ax = 0
    by = 0
    c = args[0]
    for element in args:
        if "x" in str(element):
            ax = 0 if re.match(r'^-?\d*', str(element)) is None else re.match(r'^-?\d*', str(element)).group(0)
            if ax == "-":
                ax = -1
            elif ax == "":
                ax = 1
        if "y" in str(element):
            by = 0 if  re.match(r'^-?\d*', str(element)) is None else re.match(r'^-?\d*', str(element)).group(0)
            if by == "-":
                by = -1
            elif by == "":
                by=1
    return equation_answer(ax, by, c)

def equation_answer(ax, by, c, round = 0):
    return f"{{1:NUMERICAL:={ax}:0.{round}#OK*x + 1:NUMERICAL:={by}:0.{round}#OK*y + 1:NUMERICAL:={c}:0.{round}#OK}}"






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
    return f"{{1:NUMERICAL:={ax}:0.{round}#OK}}*x + {{1:NUMERICAL:={by}:0.{round}#OK}}*y + {{1:NUMERICAL:={c}:0.{round}#OK}}"

def convert_plane_equation(args):
    ax = 0
    by = 0
    zy=0
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
        if "z" in str(element):
            zy = 0 if  re.match(r'^-?\d*', str(element)) is None else re.match(r'^-?\d*', str(element)).group(0)
            if zy == "-":
                zy = -1
            elif zy == "":
                zy=1
    return equation_plane_answer(ax, by, zy, c)

def equation_plane_answer(ax, by, zy, c, round = 0):
    return f"{{1:NUMERICAL:={ax}:0.{round}#OK}}*x + {{1:NUMERICAL:={by}:0.{round}#OK}}*y + {{1:NUMERICAL:={zy}:0.{round}#OK}}*z + {{1:NUMERICAL:={c}:0.{round}#OK}}"

def rational_plane(mt):
    ax=mt[0]
    by=mt[1]
    cz=mt[2]

    x = f'{number_convert(ax.p)} / {number_convert(ax.q)}'
    y = f'{number_convert(by.p)} / {number_convert(by.q)}'
    z = f'{number_convert(cz.p)} / {number_convert(cz.q)}'
    return f"{x}, {y}, {z}"

def point_answer(point, round = 0):
    return f"({{1:NUMERICAL:={point[0]}:0.{round}#OK}}, {{1:NUMERICAL:={point[1]}:0.{round}#OK}})"

def sqrt_view_answer(answer):
    if answer.is_Integer:
        return number_convert(answer)
    if answer.is_Rational:
        return rational_view(answer)
    if answer.is_Pow:
        return sqrt_view(answer.args[0])
    if answer.is_Mul:
        if answer.args[0].is_Integer:
            return f'{number_convert(answer.args[0])} * {sqrt_view(answer.args[1])}'
        else:
            return f'{rational_view(answer.args[0])} * {sqrt_view(answer.args[1])}'


def rational_view(number):
    return f'{number_convert(number.p)} / {number_convert(number.q)}'

def sqrt_view(sqr):
    return f'√{number_convert(sqr._args[0])}'

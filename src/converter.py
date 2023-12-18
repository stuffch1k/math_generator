from schemas import TopicWithCompexity
import xml.etree.ElementTree as ET
import html

# def xml_converter(title, task):
#     xml_task = ET.Element('question', type = 'cloze')
#     name = ET.Element('name')
#     tname = ET.Element('text')
#     tname.text = title
#     name.append(tname)
#     question = ET.Element('questiontext', format="html")
#     tquestion = ET.Element('text')
#     text = task["task"]
#     data = task["data"]
#     answer = task["answer"]
#     ctext = text
#     ctask = create_matrix_ctask(data)
#     canswer = create_matrix_canswer(answer)
#     tquestion.text = f"<![CDATA[<p>{ctext}</p><p>{ctask}</p><p>Ответ: {canswer}</p>]]>" 
#     question.append(tquestion)
#     xml_task.append(name)
#     xml_task.append(question)
#     print(xml_task)
#     return xml_task

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





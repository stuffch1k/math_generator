from schemas import TopicWithCompexity
import xml.etree.ElementTree as ET
import html

def xml_converter(title, task):
    xml_task = ET.Element('question', type = 'cloze')
    name = ET.Element('name')
    tname = ET.Element('text')
    tname.text = title
    name.append(tname)
    question = ET.Element('questiontext', format="html")
    tquestion = ET.Element('text')
    text = task["task"]
    data = task["data"]
    answer = task["answer"]
    ctext = text
    ctask = create_matrix_ctask(data)
    canswer = create_matrix_canswer(answer)
    tquestion.text = f"<![CDATA[<p>{ctext}</p><p>{ctask}</p><p>Ответ: {canswer}</p>]]>" 
    question.append(tquestion)
    xml_task.append(name)
    xml_task.append(question)
    print(xml_task)
    return xml_task

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



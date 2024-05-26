import generators as gen

from jinja2 import Environment, FileSystemLoader, select_autoescape
import numpy as np
import os
from random import randint

path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'./templates_xml')

# настройки шаблонизатора
env = Environment(
    loader=FileSystemLoader(path),
    autoescape=select_autoescape(['xml'])
)

# название категории для всего теста
test_category_name = 'Контрольная по линейной алгебре'


def convert_to_moodle(test, category_count, v=1):
    templates = []
    common_category = f"Тест по алгебре вар.{randint(1,100)}"
    for category_name, topic_count in category_count.items():
        if topic_count != 0:
            template = env.get_template('template_category.xml')
            rendered_test_category = template.render(category_name = common_category+"/"+category_name)
            tasks = create_task(test, category_name, category_count, v)
            template = env.get_template('template_question_cloze.xml')
            rendered_tasks = template.render(tasks = tasks)
            template = env.get_template('template_test.xml')
            rendered_test = template.render(
                parent_category = rendered_test_category,
                tasks_with_categories = rendered_tasks
            )
            templates.append(rendered_test)
    template = env.get_template('final.xml')
    rendered_temp = template.render(common_category = common_category,rendered_templates = templates)
    return rendered_temp
    
    

def create_task(test, category_name, catetegory_count, v=1):
    tasks = []
    for task in test:
        if v==1:
            topic = task["topic"]
            text = task["moodle_task"]
        else:
            topic = task.topic
            text = task.moodle_task
        if topic == category_name:
            tasks.append({
            'id': str(np.random.randint(1000000, 9999999)),
            'name': topic + f' - вариант {str(np.random.randint(1, 9999))}',
            'text': text
            })
    return tasks
        
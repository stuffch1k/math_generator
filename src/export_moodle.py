import generators as gen

from jinja2 import Environment, FileSystemLoader, select_autoescape
import numpy as np

# настройки шаблонизатора
env = Environment(
    loader=FileSystemLoader('./templates_xml'),
    autoescape=select_autoescape(['xml'])
)

# название категории для всего теста
test_category_name = 'Контрольная по линейной алгебре'


# генерируем варианты заданий одного типа
task_title = 'Решение СЛУ: метод Крамера'
tasks = [{
    'id': str(np.random.randint(1000000, 9999999)),
     'name': task_title + f' - вариант {1}',
     'text': gen.GenerateSolveLinearEquationTask()['moodle_task']
     },{
    'id': str(np.random.randint(1000000, 9999999)),
     'name': task_title + f' - вариант {2}',
     'text': gen.GenerateSolveLinearEquationTask()['moodle_task']
     }
]

# заполняем шаблон вопроса сгенерированными варианами задание-ответ
template = env.get_template('template_question_cloze.xml')
rendered_tasks = template.render(tasks = tasks)

# заполнеяем шаблон папки-категории для вопросов одного типа
template = env.get_template('template_category.xml')
rendered_test_category = template.render(category_name = task_title)

# собираем в общий шаблон
template = env.get_template('template_test.xml')
rendered_test = template.render(
    parent_category = rendered_test_category,
    tasks_with_categories = rendered_tasks
)

print(rendered_test)

with open('out.xml', 'w') as f:
    f.write(rendered_test)

#print(gen.GenerateSolveLinearEquationTask()['moodle_task'])
#print(gen.GenerateScalarVectorMultiplicationTask()['moodle_task'])


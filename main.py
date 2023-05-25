from jinja2 import Environment, FileSystemLoader
import json

TEMPLATE_NAME = 'story.html'
DATA_NAME = 'story.json'
SAVE_DIR = './output'

with open(f'./data/{DATA_NAME}') as f:
    data = json.load(f)

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template(TEMPLATE_NAME)
output = template.render(data=data)

with open(f'{SAVE_DIR}/{DATA_NAME[:-5]}.html', 'w') as f:
    f.write(output)
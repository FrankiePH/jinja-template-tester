from jinja2 import Environment, FileSystemLoader
import json

TEMPLATE_NAME = 'json_render.html'
DATA_NAME = 'Example Scenario.json'
SAVE_DIR = './output'

with open(f'./data/{DATA_NAME}') as f:
    data = json.load(f)

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template(TEMPLATE_NAME)
output = template.render(json_data=data)

with open(f'{SAVE_DIR}/{DATA_NAME[:-4]}.html', 'w') as f:
    f.write(output)
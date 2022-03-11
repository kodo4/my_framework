from os.path import join
from jinja2 import Template


def render(template_name, folder='templates', **kwargs):
    """

    :param template_name: имя шаблона
    :param folder: папка с шаблоном
    :param kwargs: параметры, передаваемые в шаблон
    :return:
    """
    file_path = join(folder, template_name)
    # Открываем файл на чтение
    with open(file_path, encoding='utf-8') as f:
        # Читаем
        template = Template(f.read())
    # Рендерим шаблон, внеся параметры
    return template.render(**kwargs)

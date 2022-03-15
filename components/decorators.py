# Декораток для реализации маршрутизации
class AppRoute:
    def __init__(self, routes, url):
        """
        Сохраняем значение переданного парметра
        :param routes: словарь роутов
        :param url: путь
        """
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        """
        Сам декоратор
        :param cls: объект класса контроллера
        """
        self.routes[self.url] = cls()

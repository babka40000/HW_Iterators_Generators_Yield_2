import datetime


def decorator(log_name):
    def _decorator(old_func):
        def new_func(*arg, **kwarg):
            with open(log_name, "a", encoding="utf-8") as file:
                res = old_func(*arg, **kwarg)
                file.write(
                    f'Дата: {datetime.date.today()}, время: {datetime.datetime.now()}, имя функции: {old_func.__name__}, '
                    f'параметры: {arg} {kwarg}, результат: {res}\n')
                return res

        return new_func
    return _decorator

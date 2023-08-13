def pylounge_decorator(func):
    def wrapper():
        print('Всем привет!')
        func()
        print('Пока!')
    return wrapper


@pylounge_decorator
def get_pylounge_links():
    print('Вк, Telegram, Instagram, Twitter')


get_pylounge_links()

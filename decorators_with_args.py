def i_am_top(func):
    def wrapper(*args, **kwargs):
        print('Я наверху!')
        func(*args, **kwargs)
    return wrapper


def pylounge_decorator(func):
    def wrapper(*args, **kwargs):
        print('Всем привет!')
        func(*args, **kwargs)
        print('Пока!')
    return wrapper


@i_am_top
@pylounge_decorator
def get_pylounge_links(vk, tg, inst, tw):
    print(f'Вк - {vk}, Telegram - {tg}, Instagram - {inst}, Twitter - {tw}')


get_pylounge_links('Вконтакте', 'Телега', 'Инста', 'Твич')

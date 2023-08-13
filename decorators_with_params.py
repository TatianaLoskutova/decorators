def pylounge_decorator(hi_msg, bye_msg):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            print(hi_msg)
            func(*args, **kwargs)
            print(bye_msg)
        return wrapper
    return inner_decorator


@pylounge_decorator('Здарова!', 'Всем пока!!!')
def get_pylounge_links(vk, tg, inst, tw):
    print(f'Вк - {vk}, Telegram - {tg}, Instagram - {inst}, Twitter - {tw}')


get_pylounge_links('Вконтакте', 'Телега', 'Инста', 'Твич')

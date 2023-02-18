def str_func(in_line):
    # добавил docstring
    """
    Функция принимает на вход строку и возвращает ее со всеми заглавными буквами.
    :param in_line: str
    :return: result: in_line str with upper()
    """
    result = in_line.upper()
    return result

def str_func_title(in_line):
    # добавил коммент на GitHub
    """
    Функция принимает на вход строку и возвращает каждое слово с заглавными буквами
    :param in_line: str
    :return: str with tittle
    """
    list_str = in_line.split()
    result_str = ''
    for word in list_str:
        result_str += word.tittle()

    return result_str

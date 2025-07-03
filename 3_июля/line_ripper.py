import sys


def get_groups(source: list[str], group_size: int) -> list[list[str]]:
    """
    Преобразует список строк в список групп строк по N элементов.
    Остаточные строки, не формирующие заполненную группу, игнорируются.
    :param source:      Исходный список строк.
    :param group_size:  По сколько элементов берётся в группу.
    :return:            Список групп строк по N элементов.
    """
    result = []
    next_group = []
    for line in source:
        next_group.append(line)
        if len(next_group) == group_size:
            result.append(next_group.copy())
            next_group.clear()
    return result


def filter_parity(lines: list[str]) -> list[str]:
    """
    Функция принимает список строк и возвращает список тех слов из них,
    чётность которых совпадает с чётностью суммарной длины строк.
    :param lines:   Полученный список строк.
    :return:        Список слов, чётность которых совпадает с чётностью
                    суммарной длины строк.
    """
    lines_parity = sum(map(lambda s: len(s), lines)) % 2 == 0
    words = []
    for line in lines:
        for word in line.split():
            if len(word) % 2 == lines_parity:
                words.append(word)
    return words


def distinct_and_sort(words: list[str]) -> list[str]:
    """
    Функция принимает список слов, приводит первую букву в каждом
    к верхнему регистру, остальные буквы к нижнему,
    и возвращает список уникальных слов,
    сортированный по лексикографическому возрастанию.
    :param words:   Список слов.
    :return:        Отсортированный список уникальных слов c большой буквы.
    """
    return sorted(list(set(map(lambda s: s.capitalize(), words))))


def output(words: list[str], limit: int) -> None:
    """
    Выводит на печать через точку пробелом полученный список слов,
    но не более, чем N слов.
    :param words:   Список печатаемых слов.
    :param limit:   Максимальное количество слов для вывода.
    """
    print('. '.join(words[:limit]))
    # for _ in range(limit):
    #     if words:
    #         print(words.pop(0), end='. ')


def process(text: list[str], group_size: int, limit: int) -> None:
    """
    Процедура обработки и вывода текста согласно заданию.
    :param text: Вводимый текст в виде списка строк (в формате stdin)
    :param group_size: По сколько строк берётся в группу
    :param limit: Сколько слов выводить
    """
    for group in get_groups(text, group_size):
        words = filter_parity(group)
        output(distinct_and_sort(words), limit)

def prepare_text(text: str) -> list[str]:
    """
    Функция, разбирающая текст на строки с символом перевода строки в конце каждой.
    Эмулирует ввод строк из stdin.
    :param text: Текст в виде многострочной строки
    :return: Массив строк, завершающихся символом перевода строки (если он присутствует)
    """
    return list(map(lambda l: l + '\n', text.split('\n')))


def main():

    text1 = """I know it sounds ridiculous
    but there is an old opera tradition
    associated with the eighth box
    complete nonsense
    You see this box is haunted
    Mr. Bucket mumbled"""

    text2 = """Nanny Ogg had seen a lot of strange things
    some of them even twice
    She saw elves walking stones
    Once an entire house fell on her head
    But she had never seen
    Granny Weatherwax rouged
    She witnessed a unicorn being shod"""

    group_size = 3
    output_limit = 5

    process(prepare_text(text1), group_size, output_limit)
    process(prepare_text(text2), group_size, output_limit)

    process(sys.stdin.readlines(),
            group_size, output_limit)

main()

import json
from datetime import date


def load_data():
    """
    Загружает данные из файла
    """
    with open("src/operations.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def distribation_by_dates(data):
    """
    Распределяет даты по убыванию, отбирает выполненые операции и удаляет пустые словари
    :param data: исходные данные
    :return: данные по убыванию даты (5шт)
    """
    result_data = []
    for i in data:
        if i == {}:
            continue
        elif i['state'] == 'EXECUTED':
            result_data.append(i)
    sort_data = sorted(result_data, key=lambda item: item['date'], reverse=True)
    return sort_data[0:5]

def date_operation(item):
    """
    Возвращает дату операции в новом формате
    :param item: исходные данные
    :return: дату операции
    """
    date_1 = item['date'].split('T')
    date_operations = date.fromisoformat(date_1[0]).strftime("%d.%m.%Y")
    return date_operations

def from_check_operation(item):
    """
    Преобразует номер счета списания
    :param item: исходные данные
    :return: вывод счета в правильном формате
    """
    if 'from' not in item.keys():
        return ''
    else:
        from_check_card = item['from'][:-16]
        from_check_numbers = item['from'][-16:]
        from_check_for_print = f'{from_check_card} {from_check_numbers[0:4]} {from_check_numbers[4:6]}** **** {from_check_numbers[-4:]}'
        return f'{from_check_for_print} -> '


def to_check_operation(item):
    """
        Преобразует номер счет получения
        :param item: исходные данные
        :return: вывод счета в правильном формате
        """
    if 'to' not in item.keys():
        return ''
    else:
        to_check_card = item['to'][:-20]
        to_check_numbers = item['to'][-20:]
        to_check_for_print = f'{to_check_card} **{to_check_numbers[-4:]}'
        return to_check_for_print
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
    return sort_data[0:4]

def date_operation(item):
    """
    Возвращает дату операции в новом формате
    :param item: исходные данные
    :return: дату операции
    """
    date_1 = item['date'].split('T')
    date_operation = date.fromisoformat(date_1[0]).strftime("%d.%m.%Y")
    return date_operation
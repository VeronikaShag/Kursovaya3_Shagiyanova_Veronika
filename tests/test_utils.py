import pytest
from src import utils


def test_distribation_by_dates():
    assert (utils.distribation_by_dates([{"state": "EXECUTED",
                                         "date": "2019-08-26T10:50:58.294041"}, {},
                                        {"state": "EXECUTED",
                                         "date": "2018-12-20T16:43:26.929246"},
                                        {"state": "CANCELED",
                                         "date": "2018-09-12T21:27:25.241689"}]) ==
            [{"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
             {"state": "EXECUTED", "date": "2018-12-20T16:43:26.929246"}])


@pytest.fixture
def item():
    return [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58",
                            "currency": {
                                            "name": "руб.",
                                            "code": "RUB"
                                        }
                            },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }]


def test_date_operation(item):
    assert utils.date_operation(item[0]) == '26.08.2019'
    assert utils.date_operation(item[1]) == '23.03.2018'


def test_from_check_operation(item):
    assert utils.from_check_operation(item[0]) == 'Maestro 1596 83** **** 5199 -> '
    assert utils.from_check_operation(item[1]) == ''


def test_to_check_operation(item):
    assert utils.to_check_operation(item[0]) == 'Счет **9589'
    assert utils.to_check_operation(item[1]) == 'Счет **2431'

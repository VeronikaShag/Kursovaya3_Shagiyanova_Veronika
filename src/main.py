from src.utils import load_data, distribation_by_dates, date_operation, from_check_operation, to_check_operation

data = load_data()
#print(distribation_by_dates(data))
for i in distribation_by_dates(data):
    print(date_operation(i), i['description'])
    print(f'{from_check_operation(i)}{to_check_operation(i)}')
    print(i["operationAmount"]["amount"], i["operationAmount"]["currency"]["name"])
    print('')



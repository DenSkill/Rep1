import requests
from datetime import datetime


def get_data(url):
    '''
    Получает данные с внешнего ресурса,
    проверяет статус обращения к внешнему ресурсу, чтобы исключить падение программы
    :return: данные из json-файла или уровень ошибки
    '''
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "INFO: Данные получены успешно\n"
        return None, f"ERROR: status_code:{response.status_code}\n"
    #Если нет соединения
    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionError\n"
    #Если нет json-формата данных
    except requests.exceptions.JSONDecodeError:
        return None, "ERROR: requests.exceptions.JSONDecodeError\n"



def get_filtered_data(data, filtered_empty_from=False):
    '''
    сортирует данные со статусом 'EXECUTED'
    '''
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    if filtered_empty_from:
        data = [x for x in data if 'from' in x]
    return data


def get_last_values(data, count_last_values):
    '''
    сортирует данные по дате (сначала самые последние)
    выводит COUNT_LAST_VALUES последних
    '''
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    '''
    извлекает необходимые данные и переводит в нужный формат
    '''
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row['description']
        from_info, from_bill = '',''
        if 'from' in row:
            sender = row['from'].split()
            from_bill = sender.pop(-1)
            from_bill = f'{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}'
            from_info = " ".join(sender)
        to = f'{row["to"].split()[0]} **{row["to"][-4:]}'
        operation_amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'

        formatted_data.append(f"""\
{date} {description}
{from_info} {from_bill} -> {to} 
{operation_amount}""")

    return formatted_data
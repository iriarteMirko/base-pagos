from datetime import datetime

def get_last_date(dates_list: list[datetime]) -> datetime:
    last_date = dates_list[0]
    for date in dates_list:
        if date > last_date:
            last_date = date
    return last_date

def get_date(file_list: list[str]) -> str:
    dates_list = []
    for file in file_list:
        fecha_list =  file.split(' ')[-1].split('.')[:3]
        dates_list.append(datetime.strptime(fecha_list[0] + '.' + fecha_list[1] + '.' + fecha_list[2], '%d.%m.%Y'))
    return get_last_date(dates_list).strftime('%d.%m.%Y')
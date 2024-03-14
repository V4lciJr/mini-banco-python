from datetime import datetime


def date_for_str(data):
    return data.strftime('%d/%m/%Y')


def str_for_date(date_str):
    return datetime.strptime(date_str, '%d/%m/%Y')


def format_float_for_str(value):
    return f'R$ {value: ,.2f}'
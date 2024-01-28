import datetime as dt

def get_days_from_today():
    try:
        d_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
        input_date = dt.datetime.strptime(d_input, '%Y-%m-%d').date()
        today = dt.datetime.now().date()
        days = today.toordinal() - input_date.toordinal()
        if days < 0:
            print(f'До цього часу залишається {abs(days)} днів')
        elif days > 0:
            print(f'Пройшло {days} днів')
        else:
            print('Це сьогодні!')
    except ValueError:
        print('Упс, щось пiшло не так, введiть вiрний формат дати...')

while True:
    get_days_from_today()

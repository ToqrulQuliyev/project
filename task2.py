exchange_usd = float(input('Курс доллара: '))
rub = float(input('Сколько у вас рублей?: '))
usd = float(input('Сколько у вас долларов?: '))
usd_count =((usd*exchange_usd - rub)/2)/exchange_usd
rub_count = ((rub/exchange_usd - usd)/2)*exchange_usd
if rub < usd*exchange_usd:
    print('Нужно продать ', usd_count, 'долларов')
elif rub > usd*exchange_usd:
    print('Нужно продать', rub_count, 'рублей')
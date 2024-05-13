weight = float(input('Введите ваш вес (в кг.):'))
height = float(input('Введите ваш рост (в м.):'))
bmi = weight / (height**2)
print(round(bmi, 2))
if bmi <= 16:
    print('Выраженный дефицит массы тела')
elif 16 < bmi < 18.5:
    print('Недостаточная (дефицит) масса тела')
elif 18.5 < bmi < 25:
    print('Норма')
elif 25 < bmi < 30:
    print('Избыточная масса тела (предожирение)')
elif 30 < bmi < 35:
    print('Ожирение 1 степени')
elif 35 < bmi < 40:
    print('Ожирение 2 степени')
elif bmi >= 40:
    print('Ожирение 3 степени')
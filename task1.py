money_N = int(input("Сколько у вас денег?\n"))
years = int(input('На сколько лет хотите сделать вклад?\n'))
for i in range(years):
    bank = money_N + money_N * (10/100)
    money_N = bank
print("По итогу вы получите", money_N,'рублей')
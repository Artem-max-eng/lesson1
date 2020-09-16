a = input("Как вас зовут? ")
print(f'Пошел нахуй, {a}!')
b = int(input("Сколько вам лет? "))
if (b < 18):
    print('Не получилось, не фартануло(') 
elif (b > 18): 
    print('Welcome to the club, buddy!')
else:    
    print(f'Неплохо тебя жизнь поматала, я в свои {b} еще в горшок ходил...')

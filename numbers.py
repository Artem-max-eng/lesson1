stock = {
    'city':'Moskva',
    'temperature': '20',
    'date': '27.05.2019',
    'country': 123
}
stock['temperature'] = int(stock['temperature']) - 5
print(stock)
if 'country' not in stock:
    stock['country'] = 'Russia'
    print(stock)
else:
    print('alreadyexists')


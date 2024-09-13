number = ['3', '5', '7', '9', '10.5']
print(number)
number.append('Python')
count = len(number)
print(count)
print(number[0])
print(number[5])
print(number[1:4])
del number[5]
print(number)
count = len(number)
print(count)
stock = {
    "city": "Москва",
    "temperature": 20
}
print(stock["city"])
stock['temperature'] = stock['temperature'] - 5
print(stock['temperature'])
print(stock)
print(stock.get("country"))
stock["country"] = "Россия"
print(stock)
stock["date"] = "27.05.2019"
print(stock)
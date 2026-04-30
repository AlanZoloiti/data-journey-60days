data = [100, -20, 0, 50, -10, 200]

positive = [x for x in data if x > 0]

tax = list(map(lambda x: x * 1.2, positive))

result = list(filter(lambda x: x > 100, tax))

print(result)

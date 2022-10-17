# def square(a):
#     return a * a


arr = [1, 2, 3, 4, 5]

print(list(map(lambda a: a * a, arr)))
print(list(filter(lambda a: a % 2 == 0, arr)))
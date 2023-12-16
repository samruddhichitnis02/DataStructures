import random
random.seed("Bubble")

numbers = [random.randint(0, 500) for i in range(10)]

print(numbers)
n = len(numbers) - 1

for i in range(n * n):
    pos = i % n
    if numbers[pos] > numbers[pos + 1]:
        numbers[pos], numbers[pos + 1] = numbers[pos + 1], numbers[pos]

print(numbers)
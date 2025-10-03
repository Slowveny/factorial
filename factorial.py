number = int(input('Enter a number: '))
result = 1

for i in range(1, number + 1):
    result = result * i

print(f'The factorial of the number {number} is {result}')
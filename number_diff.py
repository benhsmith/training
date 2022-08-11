import random
import time

def get_numbers():
    rand = lambda : random.randint(1,10)

    numbers = [rand()]

    while len(numbers) < 2:
        num = rand()

        last_diff = abs(num - numbers[len(numbers) - 1])

        if num not in numbers and last_diff > 1:
            numbers.append(num)

    return numbers

def find_answer(numbers):
    return abs(numbers[1] - numbers[0])

last_answer = True
while True:
    if last_answer:
        numbers = get_numbers()
    print(f'{numbers[0]}     {numbers[1]}')

    answer = find_answer(numbers)

    while True:
        start = time.time()
        response = input()
        end = time.time()

        elapsed = end - start

        try:
            last_answer = int(response) == answer
            break
        except ValueError:
            continue

    if not last_answer:
        print(f'* Incorrect')

    if (elapsed > 2):
        last_answer = False
        print(f'* Time: {elapsed}')
    print('')


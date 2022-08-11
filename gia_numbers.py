import random
import time

def get_numbers():
    rand = lambda : random.randint(0,20)

    numbers = [rand()]

    while True:
        while len(numbers) < 3:
            num = rand()
            #print(f'randint: {num}')

            last_diff = abs(num - numbers[len(numbers) - 1])

            if num not in numbers and (
                last_diff > 1 and last_diff < 5
            ):
                numbers.append(num)

        if find_answer(numbers) != 0:
            break
        else:
            # retry
            #print("retry")
            numbers = [rand()]

    return numbers

def find_answer(numbers):
    if len(numbers) != 3:
        return 0

    numbers = sorted(numbers)
    dist0 = numbers[1] - numbers[0]
    dist1 = numbers[2] - numbers[1]

    if dist0 == 1 or dist1 == 1:
        return 0

    if dist0 > dist1:
        return numbers[0]
    elif dist0 < dist1:
        return numbers[2]
    else:
        return 0

last_answer = True

while True:
    if last_answer:
        numbers = get_numbers()
    print(f'{numbers[0]}     {numbers[1]}      {numbers[2]}')

    start = time.time()
    response = input()
    end = time.time()

    elapsed = int(end - start)

    answer = find_answer(numbers)
    last_answer = int(response) == answer

    if not last_answer:
        print(f'* Incorrect: {answer}')

    if (elapsed > 4):
        print(f'* Time: {elapsed}')
    print('')


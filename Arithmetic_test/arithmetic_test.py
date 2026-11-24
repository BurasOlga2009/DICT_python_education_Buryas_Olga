import random

num1 = random.randint(2, 9)
num2 = random.randint(2, 9)
operation = random.choice(['+', '-', '*'])

print(f"{num1} {operation} {num2}")

if operation == '+':
    correct_answer = num1 + num2
elif operation == '-':
    correct_answer = num1 - num2
else:
    correct_answer = num1 * num2

user_answer = int(input())

if user_answer == correct_answer:
    print("Right!")
else:
    print("Wrong!")

import random

score = 0

for _ in range(5):
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operation = random.choice(['+', '-', '*'])
    print(f"{num1} {operation} {num2}")

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    while True:
        try:
            user_answer = int(input())
            break
        except ValueError:
            print("Incorrect format.")

    if user_answer == correct_answer:
        print("Right!")
        score += 1
    else:
        print("Wrong!")

print(f"Your mark is {score}/5.")


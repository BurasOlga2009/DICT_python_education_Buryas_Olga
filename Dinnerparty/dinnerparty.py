import random
num_people = int(input("Enter the number of friends joining (including you):\n> "))
if num_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends_dict = {}
    for _ in range(num_people):
        name = input("> ")
        friends_dict[name] = 0
    print(friends_dict)


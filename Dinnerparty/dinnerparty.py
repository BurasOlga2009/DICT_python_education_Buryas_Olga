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
total_amount = float(input("Enter the total amount:\n> "))

share = round(total_amount / num_people, 2)
for name in friends_dict:
    friends_dict[name] = share
print(friends_dict)
lucky_choice = input('Do you want to use the "Who is the lucky?" feature? Write Yes/No:\n> ')

if lucky_choice == "Yes":
        lucky_name = random.choice(list(friends_dict.keys()))
        print(f"\n{lucky_name} is the lucky one!")
else:
        print("No one is going to be lucky")
if lucky_choice == "Yes":
    lucky_name = random.choice(list(friends_dict.keys()))
    print(f"\n{lucky_name} is the lucky one!")

    new_share = round(total_amount / (num_people - 1), 2)

    for name in friends_dict:
        if name == lucky_name:
            friends_dict[name] = 0
        else:
            friends_dict[name] = new_share

    print(friends_dict)
else:
    print("No one is going to be lucky")
    print(friends_dict)
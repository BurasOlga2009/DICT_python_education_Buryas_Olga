def main():
    pencils = int(input("How many pencils would you like to use:\n"))
    first_player = input("Who will be the first (Olga, Vitaliy):\n")
    print("|" * pencils)
    print(f"{first_player} is going first!")
if __name__ == "__main__":
    main()

def main():
    pencils = int(input("How many pencils would you like to use:\n"))
    current_player = input("Who will be the first (Olga, Vitaliy):\n")
    while pencils >0:
        print("|" * pencils)
        print(f"{current_player}'s turn:")
        taken = int(input())
        pencils -= taken
        current_player = "Olga" if current_player == "Vitaliy" else "Vitaliy"
if __name__ == "__main__":
    main()

def main():
    print("How many pencils would you like to use:")
    while True:
        pencils_input = input()
        if not pencils_input.isdigit():
            print("The number of pencils should be numeric")
            continue
        pencils = int(pencils_input)
        if pencils == 0:
            print("The number of pencils should be positive")
            continue
        break

    print("Who will be the first (Olga, Vitaliy):")
    while True:
        current_player = input()
        if current_player not in ["Olga", "Vitaliy"]:
            print("Choose between 'Olga' and 'Vitaliy'")
            continue
        break

    while pencils > 0:
        print("|" * pencils)
        print(f"{current_player}'s turn:")
        while True:
            taken_input = input()
            if taken_input not in ["1", "2", "3"]:
                print("Possible values: '1', '2' or '3'")
                continue
            taken = int(taken_input)
            if taken > pencils:
                print("Too many pencils were taken")
                continue
            break

        pencils -= taken
        current_player = "Olga" if current_player == "Vitaliy" else "Vitaliy"

    print(f"{current_player} won!")


if __name__ == "__main__":
    main()









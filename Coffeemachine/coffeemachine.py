print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")

print("Write how many cups of coffee you will need:")
cups = int(input())
water = cups * 200
milk = cups * 50
beans = cups * 15
print(f"For {cups} cups of coffee you will need:")
print(f"{water} ml of water")
print(f"{milk} ml of milk")
print(f"{beans} g of coffee beans")

print("Write how many ml of water the coffee machine has: ")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
beans = int(input())
print("Write how many cups of coffee you will need:")
cups_needed = int(input())
possible_cups = min(water // 200, milk // 50, beans // 15)
if possible_cups == cups_needed:
    print("Yes, I can make that amount of coffee")
elif possible_cups > cups_needed:
    extra_cups = possible_cups - cups_needed
    print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that)")
else:
    print(f"No, I can make only {possible_cups} cups of coffee")

water = 400
milk = 540
beans = 120
cups = 9
money = 550
def print_stage():
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of beans")
    print(f"{cups} of cups")
    print(f"{money} of money")
def buy():
    global water, milk, beans, cups, money
    print("What do you want to buy? 1 - espresso, 2 - macchiato, 3 - raf:")
    choice = input()
    if choice == "1":
        water -= 250
        beans -= 16
        cups -= 1
        money += 5
    elif choice == "2":
        water -= 250
        beans -= 16
        milk -= 100
        cups -= 2
        money += 7
    elif choice == "3":
        water -= 350
        milk -= 150
        cups -= 1
        money += 3
def fill():
    global water, milk, beans, cups
    print("Write how many ml of water you want to add:")
    water += int(input())
    print("Write how many ml of milk you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans you want to add:")
    beans += int(input())
    print("Write how many disposable coffee cups you want to add:")
    cups += int(input())
def take():
    global money
    print(f"I gave you {money}")
    money = 0
print_stage()
print("\nWrite action (buy, fill, take):")
action = input()
if action == "buy":
    buy()
elif action == "fill":
    fill()
elif action == "take":
    take()
print()
print_stage()

water = 400
milk = 540
beans = 120
cups = 9
money = 550


def print_state():
    print("\nThe coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")


def make_coffee(need_water, need_milk, need_beans, cost):
    global water, milk, beans, cups, money

    if water < need_water:
        print("Sorry, not enough water!")
    elif milk < need_milk:
        print("Sorry, not enough milk!")
    elif beans < need_beans:
        print("Sorry, not enough coffee beans!")
    elif cups < 1:
        print("Sorry, not enough disposable cups!")
    else:
        print("I have enough resources, making you a coffee!")
        water -= need_water
        milk -= need_milk
        beans -= need_beans
        cups -= 1
        money += cost


def buy():
    print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    choice = input()

    if choice == "1":
        make_coffee(250, 0, 16, 4)
    elif choice == "2":
        make_coffee(350, 75, 20, 7)
    elif choice == "3":
        make_coffee(200, 100, 12, 6)
    elif choice == "back":
        return


def fill():
    global water, milk, beans, cups
    print("\nWrite how many ml of water you want to add:")
    water += int(input())
    print("Write how many ml of milk you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans you want to add:")
    beans += int(input())
    print("Write how many disposable coffee cups you want to add:")
    cups += int(input())


def take():
    global money
    print(f"\nI gave you {money}")
    money = 0


while True:
    print("\nWrite action (buy, fill, take, remaining, exit):")
    action = input()

    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        print_state()
    elif action == "exit":
        break

class CoffeeMachine:
    def init(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "choosing_action"
        self.prompt()

    def prompt(self):
        prompts = {
            "choosing_action": "\nWrite action (buy, fill, take, remaining, exit):",
            "choosing_coffee": "\nWhat do you want to buy? 1 - espresso, 2 - macchiato, 3 - raf, back - to main menu:",
            "filling_water": "\nWrite how many ml of water you want to add:",
            "filling_milk": "Write how many ml of milk you want to add:",
            "filling_beans": "Write how many grams of coffee beans you want to add:",
            "filling_cups": "Write how many disposable coffee cups you want to add:",
        }
        if self.state in prompts:
            print(prompts[self.state])

    def handle_input(self, user_input: str):
        if self.state == "choosing_action":
            self._handle_action(user_input)
        elif self.state == "choosing_coffee":
            self._buy_coffee(user_input)
        elif self.state == "filling_water":
            self.water += int(user_input)
            self.state = "filling_milk"
        elif self.state == "filling_milk":
            self.milk += int(user_input)
            self.state = "filling_beans"
        elif self.state == "filling_beans":
            self.beans += int(user_input)
            self.state = "filling_cups"
        elif self.state == "filling_cups":
            self.cups += int(user_input)
            self.state = "choosing_action"

        if self.state != "exit":
            self.prompt()

    def _handle_action(self, action: str):
        if action == "buy":
            self.state = "choosing_coffee"
        elif action == "fill":
            self.state = "filling_water"
        elif action == "take":
            print(f"\nI gave you {self.money}")
            self.money = 0
        elif action == "remaining":
            self._print_remaining()
        elif action == "exit":
            self.state = "exit"

    def _buy_coffee(self, choice: str):
        if choice == "back":
            self.state = "choosing_action"
            return

        # Рецепты: 1 - espresso, 2 - macchiato, 3 - raf
        recipes = {
            "1": {"water": 250, "milk": 0, "beans": 16, "cost": 4},     # espresso
            "2": {"water": 350, "milk": 75, "beans": 20, "cost": 7},    # macchiato
            "3": {"water": 200, "milk": 100, "beans": 12, "cost": 6},   # raf
        }

        recipe = recipes.get(choice)
        if not recipe:
            self.state = "choosing_action"
            return

        if self.water < recipe["water"]:
            print("Sorry, not enough water!")
        elif self.milk < recipe["milk"]:
            print("Sorry, not enough milk!")
        elif self.beans < recipe["beans"]:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= recipe["water"]
            self.milk -= recipe["milk"]
            self.beans -= recipe["beans"]
            self.cups -= 1
            self.money += recipe["cost"]

        self.state = "choosing_action"

    def _print_remaining(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")


def main():
    machine = CoffeeMachine()
    while machine.state != "exit":
        user_input = input()
        machine.handle_input(user_input)


if __name__ == "__main__":
    main()


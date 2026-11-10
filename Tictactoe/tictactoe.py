def main():
    print("X 0 X")
    print("0 X 0")
    print("X X 0")
if __name__ == "__main__":
    main()

def main():
    cells = input("Enter cells: ")
    print("---------")
    print(f"| {cells[0]} {cells[1]} {cells[2]} |")
    print(f"| {cells[3]} {cells[4]} {cells[5]} |")
    print(f"| {cells[6]} {cells[7]} {cells[8]} |")
    print("---------")
if __name__ == "__main__":
    main()


def main():
    cells = input("Enter cells: ")
    grid = [c if c != '_' else ' ' for c in cells]
    print("---------")
    print(f"| {grid[0]} {grid[1]} {grid[2]} |")
    print(f"| {grid[3]} {grid[4]} {grid[5]} |")
    print(f"| {grid[6]} {grid[7]} {grid[8]} |")
    print("---------")
    x_count = cells.count('X')
    o_count = cells.count('O')
    empty_count = cells.count('_') + cells.count(' ')
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8,], [2, 4, 6]]
    x_wins = False
    o_wins = False
    for cond in win_conditions:
        if cells[cond[0]] == cells[cond[1]] == cells[cond[2]] == 'X':
            x_wins = True
        if cells[cond[0]] == cells[cond[1]] == cells[cond[2]] == 'O':
            o_wins = True

    if abs(x_count - o_count) >= 2 or (x_wins and o_wins):
        print("Impossible")
    elif x_wins:
        print("X wins")
    elif o_wins:
        print("O wins")
    elif empty_count > 0:
        print("Game not finished")
    else:
        print("Draw")
if __name__ == "main":
    main()


def print_board(grid):
    print("---------")
    print(f"| {grid} {grid} {grid} |")
    print(f"| {grid} {grid} {grid} |")
    print(f"| {grid} {grid} {grid} |")
    print("---------")


def main():
    cells = input("Enter cells: ")
    grid = [c if c != '_' else ' ' for c in cells]
    print_board(grid)

    while True:
        user_input = input("Enter the coordinates: ")
        parts = user_input.split()

        if len(parts) != 2:
            print("You should enter numbers!")
            continue

        if not (parts.isdigit() and parts.isdigit()):
            print("You should enter numbers!")
            continue

        row = int(parts)
        col = int(parts)

        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        index = (row - 1) * 3 + (col - 1)

        if grid[index] in ['X', 'O']:
            print("This cell is occupied! Choose another one!")
            continue

        grid[index] = 'X'
        print_board(grid)
        break


if __name__ == "main":
    main()



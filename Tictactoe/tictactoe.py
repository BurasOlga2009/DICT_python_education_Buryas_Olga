def main():
    print("X O X")
    print("O X O")
    print("X X O")
if __name__ == "__main__":
    main()

def print_board(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {cells[i]} {cells[i + 1]} {cells[i + 2]} |")
    print("---------")
def main():
    cells = input("Enter cells: ")
    print_board(cells)
if __name__ == "__main__":
    main()

def print_board(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {cells[i]} {cells[i + 1]} {cells[i + 2]} |")
    print("---------")


def check_winner(cells, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(
        cells[a] == cells[b] == cells[c] == player
        for a, b, c in win_conditions
    )
def analyze_state(cells):
    x_count = cells.count("X")
    o_count = cells.count("O")
    x_wins = check_winner(cells, "X")
    o_wins = check_winner(cells, "O")

    if (x_wins and o_wins) or abs(x_count - o_count) >= 2:
        return "Impossible"
    if x_wins:
        return "X wins"
    if o_wins:
        return "O wins"
    if "_" not in cells and " " not in cells:
        return "Draw"
    return "Game not finished"
def main():
    cells = input("Enter cells: ")
    print_board(cells)
    print(analyze_state(cells))
if __name__ == "main":
    main()

def print_board(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {cells[i]} {cells[i + 1]} {cells[i + 2]} |")
    print("---------")


def get_valid_move(cells):
    while True:
        coords = input("Enter the coordinates: ").split()

        if len(coords) != 2 or not (coords[0].isdigit() and coords[1].isdigit()):
            print("You should enter numbers!")
            continue

        row, col = int(coords[0]), int(coords[1])

        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        index = (row - 1) * 3 + (col - 1)
        if cells[index] != " ":
            print("This cell is occupied! Choose another one!")
            continue

        return index


def main():
    raw_cells = input("Enter cells: ").replace("_", " ")
    cells = list(raw_cells)
    print_board(cells)

    move_index = get_valid_move(cells)
    cells[move_index] = "X"
    print_board(cells)


if __name__ == "__main__":
    main()

def print_board(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {cells[i]} {cells[i + 1]} {cells[i + 2]} |")
    print("---------")


def check_winner(cells, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(
        cells[a] == cells[b] == cells[c] == player
        for a, b, c in win_conditions
    )


def analyze_state(cells):
    x_count = cells.count("X")
    o_count = cells.count("O")
    x_wins = check_winner(cells, "X")
    o_wins = check_winner(cells, "O")

    if (x_wins and o_wins) or abs(x_count - o_count) >= 2:
        return "Impossible"
    if x_wins:
        return "X wins"
    if o_wins:
        return "O wins"
    if " " not in cells:
        return "Draw"
    return "Game not finished"


def get_valid_move(cells):
    while True:
        coords = input("Enter the coordinates: ").split()

        if len(coords) != 2 or not (coords[0].isdigit() and coords[1].isdigit()):
            print("You should enter numbers!")
            continue

        row, col = int(coords[0]), int(coords[1])

        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        index = (row - 1) * 3 + (col - 1)
        if cells[index] != " ":
            print("This cell is occupied! Choose another one!")
            continue

        return index


def main():
    cells = [" "] * 9
    current_player = "X"
    print_board(cells)

    while True:
        move_index = get_valid_move(cells)
        cells[move_index] = current_player
        print_board(cells)

        state = analyze_state(cells)
        if state != "Game not finished":
            print(state)
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()


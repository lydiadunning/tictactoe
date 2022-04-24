# Build a text-based version of the Tic Tac Toe game.

def print_board(marks):
    print("     a   b   c")
    h_line = "   -------------"
    print(h_line)
    for row in marks:
        print(f"{row[0]}  | {row[1]} | {row[2]} | {row[3]} |")
        print(h_line)


# interprets text input
def decipher_location(location_code):
    row = None
    col = None
    if "1" in location_code:
        row = 0
    elif "2" in location_code:
        row = 1
    elif "3" in location_code:
        row = 2
    if "a" in location_code or "A" in location_code:
        col = 1
    elif "b" in location_code or "B" in location_code:
        col = 2
    elif "c" in location_code or "C" in location_code:
        col = 3
    return [row, col]


def validate_input(entry):
    a = len(entry) == 2
    b = "1" in entry or "2" in entry or "3" in entry
    c = "a" in entry or "b" in entry or "c" in entry or "A" in entry or "B" in entry or "C" in entry
    return a and b and c


# makes a move, turn = "x" or "o"
def move(marks, turn):
    move_incomplete = True
    while move_incomplete:
        next_location = input(f"{turn}: Where would you like to move next?")
        coords = decipher_location(next_location)
        if validate_input(next_location):
            if marks[coords[0]][coords[1]] == ' ':
                marks[coords[0]][coords[1]] = turn
                move_incomplete = False
            else:
                print("That space is taken, try another!")
        else:
            print('Please enter a single row and column, such as "1b".')
    return marks


def take_turns(current_turn):
    if current_turn == "x":
        return "o"
    else:
        return "x"


def victory_test(marks, turn):
    # row wins
    win = False
    for row in marks:
        if marks[1:4] == [f"{turn}", f"{turn}", f"{turn}"]:
            win = True
    # col wins
    for i in range(1, 4):
        if marks[0][i] == f"{turn}" and marks[1][i] == f"{turn}" and marks[2][i] == f"{turn}":
            win = True
    # diag wins
    if marks[1][2] == f"{turn}":
        if marks[0][1] == f"{turn}" and marks[2][3] == f"{turn}":
            win = True
        elif marks[0][3] == f"{turn}" and marks[2][1] == f"{turn}":
            win = True
    return win


def no_moves_test(marks):
    return " " not in marks[0] and " " not in marks[1] and " " not in marks[2]


def play():
    marks = [["1", " ", " ", " "], ["2", " ", " ", " "], ["3", " ", " ", " "]]
    win = False
    full = False
    turn = 'o'
    while not win and not full:
        print_board(marks)
        marks = move(marks, turn)
        if victory_test(marks, turn):
            win = True
        elif no_moves_test(marks):
            full = True
        else:
            turn = take_turns(turn)
    if win:
        print(f"{turn} is the winner!")
    elif full:
        print(f"No more moves are possible!")

    print_board(marks)


play()
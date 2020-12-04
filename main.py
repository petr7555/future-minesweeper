import random


def main():
    rows, columns, mines = get_user_input()
    print(f"Game, W: {columns}, H: {rows}, Mines {mines}")
    field = generate_field(rows, columns, mines)
    print_field(field)


def generate_field(rows, columns, mines):
    field = [[" " for _ in range(columns)] for _ in range(rows)]
    field = place_mines(field, rows, columns, mines)
    field = place_clues(field, rows, columns)
    return field


def place_mines(field, rows, columns, mines):
    while mines > 0:
        row = random.randint(0, rows - 1)  # inclusive range
        col = random.randint(0, columns - 1)  # inclusive range
        if field[row][col] != "x":
            field[row][col] = "x"
            mines -= 1
    return field


def place_clues(field, rows, columns):
    for row in range(rows):
        for col in range(columns):
            if field[row][col] != "x":
                number_of_adjacent_mines = get_number_of_adjacent_mines(field, rows, columns, row, col)
                if number_of_adjacent_mines > 0:
                    field[row][col] = str(number_of_adjacent_mines)
    return field


def get_number_of_adjacent_mines(field, rows, columns, row, col):
    number_of_adjacent_mines = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < rows and 0 <= j < columns:
                if field[i][j] == "x":
                    number_of_adjacent_mines += 1
    return number_of_adjacent_mines


def print_field(field):
    for row in field:
        print("|".join(["", *row, ""]))


def get_input(config):
    while True:
        input_val = input(f"Enter number of {config.name}: ")
        if not input_val.isnumeric():
            print("This is not a number.")
            continue
        input_val = int(input_val)
        for check, message in config.constraints:
            if not check(input_val):
                print(message)
                break
        else:
            return input_val


class Config:

    def __init__(self, name, constraints):
        """
        name is the name of the input
        constraints is a list of two-tuples:
            - if the validation (first element of the tuple) does not pass
            - a message (second element of the tuple) is printed
        """
        self.name = name
        self.constraints = constraints


def get_user_input():
    rows = get_input(Config("rows", [(lambda x: x >= 1, "Number of rows must be at least 1.")]))
    # could add for example: (lambda x: x % 2 == 0, "Number of columns must be even.")
    columns = get_input(Config("columns", [(lambda x: x >= 1,
                                            "Number of columns must be at least 1.")]))
    mines = get_input(
        Config("mines", [(lambda x: x <= rows * columns, "Too many mines! They don't even fit into the field!")]))
    return rows, columns, mines


if __name__ == "__main__":
    main()

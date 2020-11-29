def main():
    rows, columns, mines = get_user_input()
    print(f"Game, W: {columns}, H: {rows}, Mines {mines}")
    field = generate_field(rows, columns, mines)
    print_field(field)


def generate_field(rows, columns, mines):
    field = [[" " for _ in range(columns)] for _ in range(rows)]
    return field


def print_field(field):
    for row in field:
        print("|".join(["", *row, ""]))


def get_rows_input():
    while True:
        rows = input("Enter number of rows: ")
        if not rows.isnumeric():
            print("This is not a number.")
            continue
        rows = int(rows)
        if rows < 1:
            print("Number of rows must be at least 1.")
        else:
            return rows


def get_columns_input():
    while True:
        columns = input("Enter number of columns: ")
        if not columns.isnumeric():
            print("This is not a number.")
            continue
        columns = int(columns)
        if columns < 1:
            print("Number of columns must be at least 1.")
        else:
            return columns


def get_mines_input(rows, columns):
    while True:
        mines = input("Enter number of mines: ")
        if not mines.isnumeric():
            print("This is not a number.")
            continue
        mines = int(mines)
        if mines > rows * columns:
            # TODO has to work for ANY positive integer parameters?
            print("Too many mines! They don't even fit into the field!")
        else:
            return mines


def get_user_input():
    rows = get_rows_input()
    columns = get_columns_input()
    mines = get_mines_input(rows, columns)
    return rows, columns, mines


if __name__ == "__main__":
    main()

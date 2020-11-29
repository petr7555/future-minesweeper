def main():
    rows, columns, mines = get_user_input()
    print(rows, columns, mines)


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

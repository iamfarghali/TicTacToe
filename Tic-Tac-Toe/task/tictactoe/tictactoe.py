# Extract row by row from the given string
def make_rows(string):
    rows = []
    row = []
    for i in range(1, len(string) + 1):
        row.append(string[i - 1])
        if i % 3 == 0:
            rows.append(row)
            row = []
    return rows


# Create the field from the rows that were extracted from the given string
def make_field(rows):
    string = '---------\n'
    for i in range(len(rows)):
        string += '| '
        for j in range(len(rows[i])):
            string += rows[i][j] + ' '
        string += '|\n'
    return string + '---------'


# Check if the player entered empty field
def is_finish(field):
    return True if len([dash for row in field for dash in row if dash == '_']) == 0 else False


# Check if field has 2 (rows, cols) identical Or number of element more than the other by 2
def is_impossible(field):
    x_counter = len([x for row in field for x in row if x == 'X'])
    o_counter = len([o for row in field for o in row if o == 'O'])

    if x_counter - o_counter >= 2 or o_counter - x_counter >= 2:
        return True

    elements_counter = []
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2]:
            elements_counter.append(field[i][0])
        elif field[0][i] == field[1][i] == field[2][i]:
            elements_counter.append(field[0][i])

    if len(elements_counter) == 2:
        return True


def who_win(field):
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2]:
            return field[i][0]
        elif field[0][i] == field[1][i] == field[2][i]:
            return field[0][i]
        elif field[0][0] == field[1][1] == field[2][2]:
            return field[1][1]
        elif field[0][2] == field[1][1] == field[2][0]:
            return field[1][1]
    return 'none'


def gama_status(field):
    if is_impossible(field):
        return 'Impossible'
    winner = who_win(field)
    if winner == 'X':
        return 'X wins'
    elif winner == 'O':
        return 'O wins'
    elif not is_finish(field):
        return 'Game not finished'
    else:
        return 'Draw'


def prepare_values(row, col):
    col = int(col)
    row = int(row)
    if row == 1:
        row = 3
    elif row == 3:
        row = 1
    return row - 1, col - 1


def is_occupied(row, col):
    row, col = prepare_values(row, col)
    return rows[row][col] is not '_'


current_move = 'X'


def update_rows(row, col):
    row, col = prepare_values(row, col)
    rows[row][col] = current_move


rows = make_rows('_________')
print(make_field(rows))


while True:
    user_col, user_row = input('Enter the coordinates: ').split()
    if not user_col.isnumeric() or not user_row.isnumeric():
        print('You should enter numbers!')
    elif int(user_col) < 1 or int(user_col) > 3 or int(user_row) < 1 or int(user_row) > 3:
        print('Coordinates should be from 1 to 3!')
    elif is_occupied(user_row, user_col):
        print('This cell is occupied! Choose another one!')
        continue
    else:
        update_rows(user_row, user_col)
        current_move = 'X' if current_move == 'O' else 'O'
        print(make_field(rows))
        status = gama_status(rows)
        if status == 'X wins':
            print(status)
            break
        elif status == 'O wins':
            print(status)
            break
        elif status == 'Draw':
            print(status)
            break
        else:
            continue

'''Function'''


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    field = ''

    with open(path, 'r') as input_f:
        for line in input_f:
            field += line

        field = field.split('\n')

    return field[:-1]


def check_lines(input_line, point):
    '''
    The following functions checks the visibility from the horizontal
    perspective.
    '''
    input_line = input_line[1:-1]
    counter = 0
    start = int(input_line[0])

    for elem in input_line:
        if int(elem) >= start:
            counter += 1
            start = int(elem)

    if counter != point:
        return False

    return True


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    input_line = input_line[1:pivot+1]
    marked = input_line[pivot-1]
    if marked < max(list(input_line)):
        return False

    return True


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', \
        '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', \
        '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', \
        '*35214*', '*41532*', '*2*1***'])
    False
    """
    for elem in board:
        if '?' in elem:

            return False

    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', \
        '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', \
    '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', \
        '*35214*', '*41532*', '*2*1***'])
    False
    """
    for elem in board:

        elem = elem[1:-1]
        elem = elem.replace('*', '')
        elem = list(elem)
        copy_elem = set(elem)

        if len(elem) != len(copy_elem):
            return False

    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215',\
         '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', \
        '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', \
        '*35214*', '*41532*', '*2*1***'])
    False
    """

    for elem in board:

        if elem[0] != '*':
            result = check_lines(elem, int(elem[0]))
            if not result:
                return False

        elif elem[-1] != '*':
            elem = elem[::-1]
            result = check_lines(elem, int(elem[0]))
            if not result:
                return False

    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of \
        unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical \
        case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', \
        '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', \
        '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', \
        '*41532*', '*2*1***'])
    False
    """
    new_board = []
    for _ in range(len(board[0])):
        new_row = ''
        for col in board:
            new_row += col[_]
        new_board.append(new_row)
    new_board = new_board[1:-1]
    case = check_uniqueness_in_rows(new_board)

    if not case:
        return False

    for char in board[0]:
        if char != '*':
            index = board[0].find(char)

            column = ''
            for elem in board:
                column += elem[index]

            result = check_lines(column, int(column[0]))
            if not result:
                return False

    for rahc in board[-1]:
        if rahc != '*':
            index = board[-1].find(rahc)

            column = ''
            for elem in board:
                column += elem[index]

            column = column[::-1]
            result = check_lines(column, int(column[0]))
            if not result:
                return False

    return True


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)
    test1 = check_not_finished_board(board)
    test2 = check_uniqueness_in_rows(board)
    test3 = check_horizontal_visibility(board)
    test4 = check_columns(board)

    if not test1 or not test2 or not test3 or not test4:
        return False

    return True


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))

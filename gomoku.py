def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != ' ':
                return False
    return True

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    y_start_opening = y_end - (d_y * (length))
    x_start_opening = x_end - (d_x * (length))
    y_end_opening = y_end + d_y
    x_end_opening = x_end + d_x

    count = 0
    #Make a variable count to see number of openings
    #Count can either be 0, 1, 2
    # 0: no openings so CLOSED; 1: one opening on one side so SEMIOPEN; 2 means both sides are open so OPEN
    if y_end_opening <= (len(board)-1) and x_end_opening <= (len(board)-1):
        if board[y_end_opening][x_end_opening] == " ":
            count += 1
    else:
        pass
    if y_start_opening >= 0 and x_start_opening >= 0:
        if board[y_start_opening][x_start_opening] == " ":
            count += 1
    else:
        pass
    # print(count)

    if count == 0:
        return "CLOSED"
    elif count == 1:
        return "SEMIOPEN"
    else:
        return "OPEN"

def check_all_same_colour_between(board, col, y_start, x_start, d_y, d_x, length):
    for i in range(0, length):
        y = y_start + (d_y * i)
        x = x_start + (d_x * i)
        # print("y:", y)
        # print("x:", x)
        if board[y][x] != col:
            return False
    # print("Done Check for Length", length)
    y_prior = y_start - d_y
    x_prior = x_start - d_x
    y_after = y_start + (length * d_y)
    x_after = x_start + (length * d_x)
    if y_prior >= 0 and x_prior >= 0 and x_prior < len(board):
        if board[y_prior][x_prior] == col:
            return False
    if y_after < len(board) and x_after < len(board) and x_after >= 0:
        if board[y_after][x_after] == col:
            return False
    return True

# def check_all_same_colour_between(board, col, y_start, x_start, d_y, d_x, length):
#     for i in range(0, length):
#         y = y_start + (d_y * i)
#         x = x_start + (d_x * i)
#         if board[y][x] != col:
#             return False
#     return True

def flatten_row(board, y_start, x_start, d_y, d_x):
    flattened_row = []
    length_of_row = 0
    if d_y == 0 or d_x == 0:
        length_of_row = len(board)
    else:
        y = y_start
        x = x_start
        while x >= 0 and x < len(board) and y >= 0 and y < len(board):
            length_of_row += 1
            y += d_y
            x += d_x
    for i in range(length_of_row):
        y = y_start + (i * d_y)
        x = x_start + (i * d_x)
        flattened_row.append(board[y][x])
    return flattened_row

#open_seq, semi_open_seq = detect_row(board, col, elem[0] + elem[2], elem[1] + elem[3], length + 2, elem[2], elem[3])
# def make_border_of_xs_around_board(board):
#     new_board = []
#     size = len(board)
#     new_board.append(["x"] * size)
#     for i in range(size):
#         new_board.append(board[i])
#     new_board.append(["x"] * size)
#     for i in range(len(new_board)):
#         new_board[i].insert(0, "x")
#         new_board[i].extend("x")
#     # board.insert(0, ["x"] * size)
#     # board.extend(["x"] * size)
#     # for i in range(size):
#     #     board[i].insert(0, ["x"])
#     #     board[i].append(["x"])
#     print("NEw board: ", new_board)
#     return new_board
#
# def remove_border_of_xs_around_board(board):
#     board.pop(0)
#     board.pop(-1)
#     for i in range(len(board)):
#         board[i].pop(0)
#         board[i].pop(-1)


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0
    row_empty_count = 0
    row_empty_ind = []
    # y_end += 1
    # x_end += 1
    # board = make_border_of_xs_around_board(board)
    # print_board(board)
    row = flatten_row(board, y_start, x_start, d_y, d_x)
    if " " not in row:
        # remove_border_of_xs_around_board(board)
        return 0,0
    else:
        previous_non_col = "block"
        current_run_col = 0
        for i in range(len(row)):
            if row[i] == col:
                current_run_col += 1
            elif row[i] == " ":
                if previous_non_col == "open" and current_run_col == length:
                    open_seq_count += 1
                if previous_non_col == "block" and current_run_col == length:
                    semi_open_seq_count += 1
                current_run_col = 0
                previous_non_col = "open"
            else:
                if previous_non_col == "open" and current_run_col == length:
                    semi_open_seq_count += 1
                current_run_col = 0
                previous_non_col = "block"
        if row[-1] == col and previous_non_col == "open" and current_run_col == length:
            semi_open_seq_count += 1
    # remove_border_of_xs_around_board(board)
    return (open_seq_count, semi_open_seq_count)

def find_horizontal_sequences(board, col, length):
    horizontal_sequences = []
    for i in range(len(board)):
        for start_value in range(len(board) - (length -1)):
            x_start = start_value
            x_end = start_value + (length - 1)
            if check_all_same_colour_between(board, col, i, x_start, 0, 1, length):
                horizontal_sequences.append([i, x_start, 0, 1])
    return horizontal_sequences

def find_vertical_sequences(board, col, length):
    vertical_sequences = []
    for i in range(len(board[0])):
        for start_value in range(len(board) - (length - 1)):
            y_start = start_value
            y_end = start_value + (length - 1)
            if check_all_same_colour_between(board, col, y_start, i, 1, 0, length):
                vertical_sequences.append([y_start, i, 1, 0])
    return vertical_sequences

def find_for_diagonal_sequences(board, col, length):
    for_diagonal_sequences = []
    #diagonals that start from y = 0
    for i in range(len(board) - (length -1)):
        for start_xy_value_change in range(len(board[0]) - i - (length - 1)):
            y_start = i + start_xy_value_change
            y_end = y_start + (length - 1)
            x_end = (length-1) + start_xy_value_change
            if check_all_same_colour_between(board, col, y_start, start_xy_value_change, 1, 1, length):
                for_diagonal_sequences.append([y_start, start_xy_value_change, 1, 1])
    for j in range(1, len(board[0]) - (length - 1)):
        for start_xy_value_change2 in range(len(board[0]) - j - (length - 1)):
            x_start = j + start_xy_value_change2
            x_end = x_start + (length - 1)
            y_end = (length-1) + start_xy_value_change2
            if check_all_same_colour_between(board, col, start_xy_value_change2, x_start, 1, 1, length):
                for_diagonal_sequences.append([start_xy_value_change2, x_start, 1, 1])
    return for_diagonal_sequences

def flip_board(board):
    for j in range(len(board)):
        for i in range(len(board)//2):
            board[j][i], board[j][-(i+1)] = board[j][-(i+1)], board[j][i]
    return board


def find_back_diagonal_sequences(board, col, length):
   flip_board(board)
   back_diagonal_sequences = find_for_diagonal_sequences(board, col, length)
   #X value for coordinates is wrong due to flipping so have to convert
   #Also y and x values are start not end values
   for elem in back_diagonal_sequences:
       elem[1] = (len(board)-1) - elem[1]
       elem[3] = -1
   flip_board(board)
   return back_diagonal_sequences


def find_sequences(board, col, length):
    sequences = []
    sequences.extend(find_horizontal_sequences(board, col, length))
    sequences.extend(find_vertical_sequences(board, col, length))
    sequences.extend(find_for_diagonal_sequences(board, col, length))
    sequences.extend(find_back_diagonal_sequences(board, col, length))
    return sequences


#def detect_row(board, col, y_end, x_end, length, d_y, d_x):
def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    # sequences_to_check = find_sequences(board, col, length)
    # for elem in sequences_to_check:
    #     open_seq, semi_open_seq = detect_row(board, col, elem[0], elem[1] + elem[3], length + 2, elem[2], elem[3])
    #     # print("Element is: ", elem)
    #     # count = 0
    #     # if elem[0] != 0 and elem[0] != len(board):
    #     #     print("Y:", elem[0])
    #     #     elem[0] += elem[2]
    #     #     print("Y:", elem[0])
    #     #     count += 1
    #     # if elem[1] != 0 and elem[1] != len(board):
    #     #     print("X:", elem[1])
    #     #     elem[1] += elem[3]
    #     #     print("X:", elem[1])
    #     #     count += 1
    #     # print("Length:", length)
    #     # length += count
    #     # print("Length:", length)
    #     # print("dy", elem[2], "dx", elem[3])
    #     # open_seq, semi_open_seq = detect_row(board, col, elem[0], elem[1], length, elem[2], elem[3])
    #     open_seq_count += open_seq
    #     semi_open_seq_count += semi_open_seq
    #     # length -=  count
    # return open_seq_count, semi_open_seq_count
    ####
    #Check Horizontal
    for i in range(len(board)):
        open_seq, semi_open_seq = detect_row(board, col, i, 0, length, 0, 1)
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq
    #Vertical
    for i in range(len(board[0])):
        open_seq, semi_open_seq = detect_row(board, col, 0, i, length, 1, 0)
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq
    #Diagonals
    for i in range(len(board) - length):
        open_seq, semi_open_seq = detect_row(board, col, i, 0, length, 1, 1)
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq
    for j in range(1, len(board[0]) - length):
        open_seq, semi_open_seq = detect_row(board, col, 0, j, length, 1, 1)
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq
    #Backwards Diagonals
    for i in range(len(board) - length):
        open_seq, semi_open_seq = detect_row(board, col, i, len(board) - 1, length, 1, -1)
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq
    for j in range(1, len(board[0]) - length):
        open_seq, semi_open_seq = detect_row(board, col, 0, len(board) - j - 1, length, 1, -1)
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq
    return (open_seq_count, semi_open_seq_count)




def search_max(board):
    coord_empties = []
    scores = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                coord_empties.append([i,j])
    for elem in coord_empties:
        y = elem[0]
        x = elem[1]
        board[y][x] = "b"
        scores.append(score(board))
        board[y][x] = " "
    max_score = max(scores)
    coord_max_index = scores.index(max_score)
    coord_max = coord_empties[coord_max_index]
    y, x = coord_max[0], coord_max[1]
    return (y,x)

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def is_win(board):
    if find_sequences(board, "b", 5) != []:
        return "Black won"
    elif find_sequences(board, "w", 5) != []:
        return "White won"
    elif score(board) == []:
        return "Draw"
    else:
        return "Continue playing"

def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))

def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        print(game_res)
        print(find_sequences(board, "w", 5))
        print(find_sequences(board, "b", 5))
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        print(game_res)
        print(find_sequences(board, "w", 5))
        print(find_sequences(board, "b", 5))
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    # x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    x = 4; y = 3; d_x = 1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 6
    x_end = 7

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    y = 3
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0

def testing_win_5_closed():
    board = make_empty_board(8)
    board[2][2] = "w"
    y = 3;
    x = 2;
    d_x = 0;
    d_y = 1;
    length = 5
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    if is_win(board)=="Black won":
        print("PASSSSSSSSS")
    else:
        print("EPIC FAIL :(")
        # Expected output:
        # *0|1|2|3|4|5|6|7*
        # 0 | | | | | | | *
        # 1 | | | | | | | *
        # 2 | |w| | | | | *
        # 3 | |b| | | | | *
        # 4 | |b| | | | | *
        # 5 | |b| | | | | *
        # 6 | |b| | | | | *
        # 7 | |b| | | | | *
        # *****************
        # PASSSSSSSSS

def draw_test_C():
    board = make_empty_board(8)
    for i in range(len(board)):
        put_seq_on_board(board, i, 0, 0, 1, 8, "a")
    print_board(board)
    if is_win(board)=="Draw":
        print("PASSSS CAMERON PROUD, board full of a's and your grades will be a's too")
    else:
        print("FAILED CAMERON >:(, board full of a's yet your grades will b f's")

if __name__ == "__main__":
    # board = make_empty_board(6)
    # print_board(board)
    # board[0][1] = "b"
    # board[0][2] = "b"
    # board[0][3] = "w"
    # board[0][4] = "b"
    # print_board(board)
    # print(detect_row(board, "b", 0, 5, 6, 0, 1))
    # flip_board(board)
    # print_board(board)

    #Detect Rows check
    # board = make_empty_board(6)
    # board[0][1] = "w"
    # board[0][4] = "w"
    # board[0][5] = "w"
    # board[1][2] = "w"
    # board[1][3] = "w"
    # board[1][4] = "b"
    # board[2][5] = "w"
    # board[3][2] = "w"
    # board[4][1] = "w"
    # print_board(board)
    # print(detect_rows(board, "w", 2))


    #Search Max Check
    # board = make_empty_board(6)
    # board[0][0] = "b"
    # board[0][1] = "w"
    # board[0][2] = "b"
    # board[0][3] = "b"
    # board[0][4] = "w"
    # # board[0][5] = "w"
    # board[1][0] = "b"
    # board[1][1] = "w"
    # board[1][2] = "w"
    # board[1][3] = "b"
    # board[1][4] = "w"
    # board[1][5] = "b"
    # board[2][1] = "w"
    # board[3][1] = "w"
    # board[1][3] = "w"
    # board[4][0] = "w"
    # board[2][3] = "w"
    # # print_board(board)
    # print(detect_rows(board, "w", 2))
    # print_board(board)

    # test_is_empty()
    # test_is_bounded()
    # test_detect_row()
    # test_detect_rows()
    # test_search_max()
    # easy_testset_for_main_functions()
    # some_tests()
    # testing_win_5_closed()
    # draw_test_C()
    # board = make_empty_board(7)
    # play_gomoku(7)
    # board[0][0] = "b"

    # board[1][1] = "b"
    # board[2][2] = "b"
    # board[3][3] = "b"
    # board[4][4] = "b"
    # board[5][5] = "b"
    # print_board(board)
    # print(find_sequences(board, "b", 5))
    board =  [[' ', ' ', ' ', ' ', 'w', ' ', ' ', ' '], ['w', 'w', ' ', 'b', ' ', ' ', 'w', ' '], ['w', 'w', ' ', 'b', ' ', 'b', 'w', ' '], ['w', 'b', 'b', 'b', 'b', ' ', 'w', ' '], ['b', 'b', 'w', 'b', 'b', ' ', 'w', 'w'], ['w', 'b', 'w', 'w', 'b', ' ', 'w', ' '], [' ', ' ', 'w', 'w', 'w', ' ', 'w', ' '], [' ', ' ', ' ', ' ', 'b', 'w', 'w', ' ']]
    print_board(board)
    detect_rows(board, "w", 3)







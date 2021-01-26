import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")



def make_empty_board():
    global game_over
    game_over = False
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def coord_finder(square_num):
    if square_num < 1 or square_num > 9:
        return None
    coord = []
    coord.append(((square_num - 1) // 3))
    coord.append((square_num -1) % 3)
    return coord

def put_in_board(board, mark, square_num):
    coord = coord_finder(square_num)
    board[coord[0]][coord[1]] = mark

def is_row_all_marks(board, row_i, mark):
    for i in range(3):
        if board[row_i][i] != mark:
            return False
    return True

def is_col_all_marks(board, col_i, mark):
    for i in range(3):
        if board[i][col_i] != mark:
            return False
    return True

def is_back_diag_all_marks(board, mark):
    for i in range(3):
        if board[i][i] != mark:
            return False
        # if board[i][2-i] != mark:
        #     return False
    return True

def is_for_diag_all_marks(board, mark):
    for i in range(3):
        if board[i][2-i] != mark:
            return False
    return True

def is_win(board, mark):
    global game_over
    for i in range(3):
        if is_row_all_marks(board, i, mark):
            game_over = True
            return True
        if is_col_all_marks(board, i, mark):
            game_over = True
            return True
    if is_for_diag_all_marks(board, mark) or is_back_diag_all_marks(board, mark):
        game_over = True
        return True
    return False

def play_with_self(board):
    global count
    count = 0
    mark = "X"
    while count < 9:
        square_num = input("What is the coordinate of your move:")
        print("\n")
        square_num = int(square_num)
        put_in_board(board, mark, square_num)
        # if is_win(board, mark):
        #     return "Winner"
        if mark == "X":
            mark = "O"
        else:
            mark = "X"
        count += 1
        print_board_and_legend(board)
        print("\n")
        # if is_row_all_marks(board, 0, "X"):
        #     return "Winner"


def get_free_squares(board):
    remaining_squares =[]
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                remaining_squares.append([i, j])
    return remaining_squares


def make_random_move(board, mark):
    #determine free squares
    free_squares = get_free_squares(board)
    #generate a random number between 1 and number of free squares
    num_free_squares = len(free_squares)
    #choose free square to fill (random)
    square_to_fill_index = int(num_free_squares * random.random())
    coord = free_squares[square_to_fill_index]
    board[coord[0]][coord[1]] = mark

def computer_move(board, mark):
    global count
    global game_over
    if count < 3:
        if board[1][1] == ' ':
            board[1][1] = mark
            return None
        return make_random_move(board, mark)
    free_squares = get_free_squares(board)
    #Check to see if computer can win
    for elem in free_squares:
        board[elem[0]][elem[1]] = mark
        if is_win(board, mark):
            return
        board[elem[0]][elem[1]] = ' '

    #Check to see if player will win and block it
    for elem in free_squares:
        board[elem[0]][elem[1]] = "X"
        if is_win(board, "X"):
            board[elem[0]][elem[1]] = "O"
            game_over = False
            return None
        board[elem[0]][elem[1]] = " "
    make_random_move(board, mark)


def play_against_computer(board):
    global count
    count = 0
    mark = "X"
    while count < 9 and not game_over:
        if mark == "X":
            square_num = input("What is the coordinate of your move:")
            print("\n")
            square_num = int(square_num)
            put_in_board(board, mark, square_num)
            if is_win(board, mark):
                print_board_and_legend(board)
                print("\n")
                print("Congratulations you have beat the computer")
            mark = "O"
        else:
            computer_move(board, mark)
            if is_win(board, mark):
                print_board_and_legend(board)
                print("\n")
                print("Winner is computer. Nice try!")
                return None
            mark = "X"
        count += 1
        print_board_and_legend(board)
        print("\n")
    return print("It is a Tie")




if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    print("\n\n")

    # board = [["O", "X", "X"],
    #          [" ", "X", " "],
    #          [" ", "O", " "]]
    #
    # print_board_and_legend(board)

    # #1a
    # print(coord_finder(6))
    #
    # #1b
    # put_in_board(board, "X", 9)
    # print_board_and_legend(board)

    # #1c
    # play(board)

    # #2a
    # print(get_free_squares(board))
    #
    #
    # #2b
    # make_random_move(board, "X")
    # print_board_and_legend(board)

    # #2c
    # play_against_computer(board)

    #3a
    # play_with_self(board)

    #3b
    # play_with_self(board)

    #3c
    # play_with_self(board)

    #3d
    play_against_computer(board)

    # #4a
    # play_against_computer(board)






#Needed for array() and dot()
from numpy import *


def print_matrix(M_lol):
    matrix = "["
    for i in range(len(M_lol)):
        if i < (len(M_lol) -1):
            matrix += (str(M_lol[i]) + ",\n")
        else:
            matrix += (str(M_lol[i]) + ",")
    matrix += "]"
    print(matrix)


def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)


def get_row_to_swap(M, start_i):
    index_first_non_zero = []
    for i in range(len(M)):
        if start_i == get_lead_ind(M[i]):
            return i
    return None

def add_rows_coefs(r1, c1, r2, c2):
    new_row = [0]*len(r1)
    for i in range(len(new_row)):
        new_row[i] = r1[i] * c1 + r2[i] * c2
    return new_row

def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub + 1, len(M)):
        coef = M[i][best_lead_ind]
        coef *= -1/(M[row_to_sub][best_lead_ind])
        M[i] = add_rows_coefs(M[i], 1, M[row_to_sub], coef)
    return M



def forward_step(M):
    global columns_not_all_0
    columns_not_all_0 = []
    for i in range(len(M[0])):
        for j in range(len(M)):
            if M[j][i] != 0:
                columns_not_all_0.append(i)
                break
    while len(columns_not_all_0)> len(M):
        columns_not_all_0 = columns_not_all_0[0:len(M)]
    print(columns_not_all_0)
    for elem in columns_not_all_0:
        print("column now to change:", elem)
        for i in range(columns_not_all_0.index(elem), len(M)):
            if get_lead_ind(M[i]) == elem:
                print_matrix(M)
                print("\n")
                M[columns_not_all_0.index(elem)], M[i] = M[i], M[columns_not_all_0.index(elem)]
                print_matrix(M)
                print("Done with swapping columns")
                print(columns_not_all_0.index(elem))
                print(M[columns_not_all_0.index(elem)][elem])
                # if M[columns_not_all_0.index(elem)][elem] != 1:
                #     M[columns_not_all_0.index(elem)] = add_rows_coefs(M[columns_not_all_0.index(elem)], 1/(M[columns_not_all_0.index(elem)][elem]), [0]*len(M[0]), 1)
                    # print("Needed to change coeficients in the row")
                M = eliminate(M, columns_not_all_0.index(elem), elem)
                print_matrix(M)
                print("just changed rows")
                break
    return M
                # M = eliminate(M, columns_not_all_0.index(elem), columns_not_all_0.index(elem))
                # print_matrix(M)
                # print("Changing rows below")
                # break

    # row_to_swap_with = 0
    #     for i in range(len(M)):
            # if get_lead_ind(M[i]) == i:
            #     print_matrix(M)
            #     print("\n")
            #     M[row_to_swap_with], M[i] = M[i], M[row_to_swap_with]
            #     print_matrix(M)
            #     print("Done with finding swapping columns")

def flip_matrix(M):
    for i in range(len(M)//2):
        M[i], M[-(i+1)] = M[-(i+1)], M[i]
    return M

def backward_step(M):
    print("Backward starting")
    global columns_not_all_0
    columns_not_all_0.reverse()
    print("columns:", columns_not_all_0)
    M = flip_matrix(M)
    for i in range(len(M)):
        M = eliminate(M, i, columns_not_all_0[i])
    flip_matrix(M)
    print_matrix(M)
    print("backwards end")
    return M

def make_leading_coef_1(M):
    global columns_not_all_0
    for i in range(len(M)):
        coef = M[i][get_lead_ind(M[i])]
        if coef != 1:
            for j in range(len(M[i])):
                M[i][j] = int(M[i][j] * 1/coef)
    return M

def build_augmented_matrix(M, b):
    for i in range(len(M)):
        M[i].append(b[i])
    return M

def gaussian_elimination(M):
    forward_step(M)
    backward_step(M)
    make_leading_coef_1(M)
    return M

def solve(M,b):
    x = []
    augmentedM = build_augmented_matrix(M, b)
    rnfM = gaussian_elimination(augmentedM)

    for i in range(len(rnfM)):
        x.append(rnfM[i][-1])
    return x


#Printing matrices using NumPy:
#
# #Convert a list of lists into an array:
# M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
# M = array(M_listoflists)
# #Now print it:
# print(M)
#
#
#
#
# #Compute M*x for matrix M and vector x by using
# #dot. To do that, we need to obtain arrays
# #M and x
# M = array([[1,-2,3],[3,10,1],[1,5,3]])
# x = array([75,10,-11])
# b = dot(M,x)
#
# print(b)
#
# print(M)
# #[[ 1 -2  3]
# # [ 3 10  1]
# # [ 1  5  3]]
#
# #To obtain a list of lists from the array M, we use .tolist()
# M_listoflists = M.tolist()
#
# print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

if __name__ == "__main__":
    #1
    # M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
    # print_matrix(M_listoflists)
    #
    # #2
    # print(get_lead_ind([0, 0, 2, 3]))

    #3
    # M = [[5, 6, 7, 8],
    # [0, 0, 0, 1],
    # [0, 0, 5, 2],
    # [0, 1, 0, 0]]
    # print(get_row_to_swap(M, 1))

    #4
    # print(add_rows_coefs(M[0], 1, M[1], -2))

    #5
    # M = [[5, 6, 7, 8],
    # [0,0, 1, 1],
    # [0, 0, 5, 2],
    # [0, 0, 7, 0]]
    #
    # print(eliminate(M, 1, 2))

    # #6
    # M = [[0, 0, 1, 0, 2],
    #     [1, 0, 2, 3, 4],
    #     [3, 0, 4, 2, 1],
    #     [1, 0, 1, 1, 2]]
    # M = [[1, -2, 3, 22,],
    #     [ 3, 10, 1, 314],
    #     [ 1, 5, 3, 92]]
    # M = forward_step(M)

    #7
    # M = [[1, 0, 2, 3, 4],
    #     [0, 0, 1, 0, 2],
    #     [0, 0, 0, -7, -7],
    #     [0, 0, 0, 0, 2]]
    # b = [1,
    #     2,
    #     3,
    #     4]
    #
    # M = backward_step(M)
    # M = make_leading_coef_1(M)
    #
    # print_matrix(M)

    # M = flip_matrix(M)
    # print_matrix(M)

    #8
    M = [[1, -2, 3],
        [3, 10, 1],
        [1, 5, 3]]
    b = [22, 314, 92]
    M = solve(M, b) #([75,10,-11])
    print_matrix(M)




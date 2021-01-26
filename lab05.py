def list1_start_with_list2(list1, list2):
    if len(list2) > len(list1):
        return False
    for i in range(len(list2)):
        if list2[i] != list1[i]:
            return False
    return True

def match_pattern(list1, list2):
    if len(list2) > len(list1):
        return False

    first_value = list2[0]
    for i in range(len(list1)):
        if list1[i] == first_value:
            if list1[i:len(list2) + i] == list2:
                return True

    return False

def repeats(list0):
    for i in range(len(list0) - 1):
        if list0[i] == list0[i+1]:
            return True

    return False


def print_matrix_dim(M):
    #row by columns
    row = len(M)
    columns = len(M[0])
    for i in range(len(M)):
        if len(M[i]) != columns:
            return print("Not a valid matrix")
    print(str(row) + 'x' + str(columns))

def mult_M_v_v(M, v):
    """
    Retrun value of multiplication of matrix M with vector v
    Parameters: a) M : Matrix (comes in the form of a list of lists)
                b) v: vector (comes in the form of a list)
    Function assumes matrix is a valid matrix
    """
    if len(M[0]) != len(v):
        return "DNE"
    resultant_vector = []
    for i in range(len(M)):
        row_sum = 0
        for x in range(len(M[i])):
            row_sum += (M[i][x]) * (v[x])
        resultant_vector.append(row_sum)
    return resultant_vector

def mult_M_M1(M, M1):
    """
    Retrun value of multiplication of matrix M with vector v
    Parameters: a) M : Matrix (comes in the form of a list of lists)
                b) M1: second vector (comes in the form of a list)
    Function assumes matrix is a valid matrix
    """
    if len(M) != len(M1[0]):
        return "DNE"
    resultant_matrix = [ [] for m in range(len(M))]
    for i in range(len(M)):
        for x in range(len(M1[i])):
            sum_matrix_value = 0
            for l in range(len(M1)):
                sum_matrix_value += (M[i][l]) * (M1[l][x])
            resultant_matrix[x].append(sum_matrix_value)
    return resultant_matrix



if __name__ == '__main__':
    #Problem 1
    L = [0, 1, 2, 3, 4, 5]
    M = [0, 1, 2, 3]
    N = [0, 1, 2, 3, 4, 5, 6]
    O = [1, 2, 3, 4, 5, 6]
    Q = [2, 3, 4]
    S = [2, 8, 3]
    R = [2, 5, 6, 7, 8, 8, 3, 4]
    Z = [2, 3, 4, 7, 10, 10]
    # print(list1_start_with_list2(L, M)) #True
    # print(list1_start_with_list2(M, L)) # False
    # print(list1_start_with_list2(N, L)) #True
    # print(list1_start_with_list2(N, O)) #False

    #Problem 2
    # print(match_pattern(L, Q)) # True
    # print(match_pattern(O, S)) # False

    #Problem 3
    # print(repeats(R)) #True
    # print(repeats(L)) #False
    # print(repeats(Z)) #True

    #Problem 4a
    MatrixA = [[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]]

    MatrixB = [[0, 1, 2],
               [3, 4, 5]]

    MatrixC = [[0, 1],
               [3, 4]]

    MatrixD = [[0, 1],
               [3, 4, 5]]

    # print_matrix_dim(MatrixA) # 3x3
    # print_matrix_dim(MatrixB) #2x3
    # print_matrix_dim(MatrixC) #2x2
    # print_matrix_dim(MatrixD) #Not a valid matrix


    #Problem 4b
    vectorA = [2, 1, 0]
    MatrixE = [[1, -1, 2],
               [0, -3, 1]]

    print(mult_M_v(MatrixE, vectorA)) # [1, -3]


    #Problem 4c
    MatrixF = [[2, 4, 8],
               [1, 3, 6]]
    MatrixG = [[1,9],
               [4, 2],
               [3, 7]]
    print(mult_M_M1(MatrixF, MatrixG))















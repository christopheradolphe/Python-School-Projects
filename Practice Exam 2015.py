def switch_columns(M, i, j):
    for x in range(len(M)):
        M[x][i], M[x][j] = M[x][j], M[x][i]
    return M

def is_symmetric(L):
    if L[:] == L[::-1]:
        return True
    else:
        return False

def almost_symmetric(L):
    if is_symmetric(L):
        return False
    for i in range(len(L)-1):
        original_list = L[:]
        L[i], L[i+1] = L[i+1], L[i]
        if is_symmetric(L):
            return True
        L = original_list
    return False




if __name__ == "__main__":
    Matrix = [[1, 2, 3],
              [4, 5, 6]]
    print(switch_columns(Matrix, 1, 2))

    list = [1, 2, 3, 2, 1]
    list2 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(is_symmetric(list2))

    #almost_symmetric_tests
    print(almost_symmetric(list2))



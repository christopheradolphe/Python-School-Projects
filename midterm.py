def sum_cubes(k):
    sum = 0
    for i in range(1, k+1):
        sum += i ** 3
    return sum

def sum_cubes_num_terms(n):
    sum = 0
    i = 1
    if n < 0:
        return i
    while n >= sum:
        sum += i ** 3
        if n <= sum:
            return i
        i += 1


def moving_average(measurements):
    average_list = []
    for i in range(1, len(measurements) - 1):
        sum = 0
        average = 0
        sum = measurements[i-1] + measurements[i] + measurements[i+1]
        average = sum / 3
        average_list.append(average)
    return average_list

def match(pattern, text):
    for i in range(len(pattern)):
        if pattern[i] not in text:
            return False
    text += text
    if pattern in text:
        return True
    return False

    # if text.index(pattern[0]) + len(pattern) >= len(text):
    #     if pattern in text:
    #         return True
    # else:
    #     print("else")
    #     text.extend(text)
    #     if pattern in text:
    #         return True
    # return False


def share_n1(M1, M2):
    columns = len(M1[0])
    count = 0
    flipped_matrix_M1 = []
    flipped_matrix_M2 = []
    for i in range(columns):
        columnM1 = []
        columnM2 = []
        for j in range(len(M1)):
            columnM1.append(M1[j][i])
            columnM2.append(M2[j][i])
        flipped_matrix_M1.append(columnM1)
        flipped_matrix_M2.append(columnM2)
    for x in range(len(flipped_matrix_M1)):
        for y in range(len(flipped_matrix_M2)):
            if flipped_matrix_M1[x] == flipped_matrix_M2[y]:
                count += 1
        #     if flipped_matrix_M1[i] == flipped_matrix_M2[0]:
        #         count += 1
        #     elif flipped_matrix_M1[i] == flipped_matrix_M2[1]:
        #     count += 1
        # elif flipped_matrix_M1[i] == flipped_matrix_M2[2]:
        #     count += 1
        # else:
        #     pass
    if count >= columns - 1:
        return True
    return False





if __name__ == "__main__":
    #Q1
    # print(sum_cubes(2))
    # print(sum_cubes(3)) #36
    # print(sum_cubes(1)) #1
    # print(sum_cubes(36)) #443556



    # # #Q2
    # print(sum_cubes_num_terms(10))
    # #
    # # # #Q3
    # measurements = [10.4, 1.6, 2, 0.2, 0, 0, 5.2, 0, 0, 0, 0, 0, 3.8, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 2.0, 0, 0, 0, 8.4, 2.2, 5.0]
    # print(moving_average(measurements))
    print(moving_average([1, 2, 3]))
    # #
    # #
    # #Q4
    # print(match("abc", "caqab"))


    # #Q5
    M3 = [[1, 2, 3, 5],
        [1, 5, 1, 7],
        [1, 2, 2, 6]]

    M4 = [[3, 1, 0, 5],
        [1, 1, 2, 7],
        [2, 1, 0, 6]]

    M5 = [[3, 1, 0],
        [1, 1, 2],
        [2, 1, 0]]

    M6 = [[1, 2],
           [3, 4]]

    M7 = [[2, 1],
           [7, 3]]
    #
    print(share_n1(M6, M7))






def add_neighbours(L):
    sum_list = []
    for i in range(len(L)):
        sum = 0
        if i == 0:
            sum = L[i] + L[i+1]
            sum_list.append(sum)
        elif i == len(L) - 1:
            sum = L[i-1] + L[i]
            sum_list.append(sum)
        else:
            sum = L[i-1] + L[i] + L[i+1]
            sum_list.append(sum)
    return sum_list




if __name__ == "__main__":
    #Question 4
    list1 = [1, 3, 5, 7]
    print(add_neighbours(list1))

    #Question 5
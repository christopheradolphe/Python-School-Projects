import lab02

def check_sum(n):
    total1 = 0
    for i in range(1, n+1):
        total1 += i**3

    total2 = 0
    for i in range(1, n+1):
        total2 += i
    total2 **= 2

    if total1 == total2:
        return True
    else:
        return False

def check_sums_up_to_n(N):
    for i in range(1, N+1):
        total1 = 0
        for x in range(1, i+1):
            total1 += x**3

        total2 = 0
        for x in range(1, i+1):
            total2 += x
        total2 **= 2

        if total1 == total2:
            pass
        else:
            return False

    return True


if __name__ == '__main__':
    # lab02.initialize()
    # lab02.add(42)
    # if lab02.get_current_value() == 42:
    #     print("Test 1 Passed")
    # else:
    #     print("Test 1 Failed")
    #
    #
    #problem 2
    #part 1
    # total = 0
    # n = 2
    # for i in range(1, n+1):
    #     total += i**3
    # print(total)
    #
    # #part 2
    # total = 0
    # n = 2
    # for i in range(1, n+1):
    #     total += i
    # total **= 2
    # print(total)

    # #part 3
    # print(check_sum(6))
    #
    # #part 4
    # print(check_sums_up_to_n(7))


    #Problem 4
    result = 0
    for i in range(19):
        value = ((-1)**i) / ((2*i) +1)
        result += value
    result *= 4
    print(result)











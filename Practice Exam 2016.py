def has_single_peak(L):
    increasing_or_decreasing_list = []
    count = 0
    for i in range(1, len(L)):
        if L[i] > L[i-1]:
            increasing_or_decreasing_list.append("increasing")
        if L[i] < L[i-1]:
            increasing_or_decreasing_list.append("decreasing")
    for i in range(1, len(increasing_or_decreasing_list)):
        if increasing_or_decreasing_list[i] == "increasing" and increasing_or_decreasing_list[i-1] == "decreasing":
            return False

    else:
        return True

def max_arrivals_2hrs(arrivals):
    num_arrivals = []
    for i in range(len(arrivals) - 1):
        count = 1
        start = arrivals[i]
        end = start + 120
        for x in range(i+1, len(arrivals)):
            print(end, arrivals[x])
            if arrivals[x] < end:
                count += 1
        num_arrivals.append(count)
    return max(num_arrivals)



if __name__ == "__main__":
    # L = [1, 3, 5, 4, 3, 3]
    # L2 = [2, 1, 0, 4]
    # print(has_single_peak(L))
    times = [0, 30, 40, 150, 160, 170, 370]
    print(max_arrivals_2hrs(times))



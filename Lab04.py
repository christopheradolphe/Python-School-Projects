import math

def count_evens(L):
    count = 0
    for num in L:
        if num % 2 == 0:
            count += 1
    return count

def list_to_str(lis):
    string = "'["
    for i in range(len(lis)):
        x = str(lis[i])
        string += x
        if i < (len(lis)-1):
            string += ", "
    string += "]'"
    return string

def lists_are_the_same(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

def simplify_fraction(n, m):
    if n >= m:
        min = m
    else:
        min = n
    for i in range(min):
        if m % (min - i) == 0 and n % (min - i) == 0:
            m //= (min - i)
            n //= (min- i)
    return str(n) + "/" + str(m)

def cd_int_conv(float, x):
    "Converts float values to integer values with x decimal placesfor comparison in correct_digits function"
    integer = int(float * 10 ** (x-1))
    return integer

def correct_digits(n):
    "Function that determines how many values from the Leibniz function are need to get pi correct to n digits"

    pi_n_digits = cd_int_conv(math.pi, n)

    result = 0
    numbers = 0

    while cd_int_conv(result*4, n) != pi_n_digits:
        value = ((-1)**numbers) / ((2*numbers) +1)
        result += value
        numbers += 1
    return numbers

def euclid_process(big, small):
    remainder = big % small
    while remainder != 0:
        big = small
        small = remainder
        remainder = big % small
    return small



def euclid(a, b):
    if a > b:
        gcd = euclid_process(a,b)
    else:
        gcd = euclid_process(b, a)
    return gcd

def fraction_maker(num, den):
    gcd = euclid(num, den)
    num //= gcd
    den //= gcd
    return str(num) + "/" + str(den)





if __name__ == '__main__':
    # #problem 1
    # L = [5, 7, 4, 8, 56, 401]
    # print(count_evens(L))
    #
    # #problem 2
    # print(list_to_str(L))

    # #problem 3
    # M = [5, 7, 4, 8, 56, 401]
    # J = [3, 4]
    # Q = [5, 7, 4, 8, 56, 402]
    # print(lists_are_the_same(L, M))
    # print(lists_are_the_same(L, J))
    # print(lists_are_the_same(L, Q))
    #
    # #problem 4
    # print(simplify_fraction(6, 9))
    # print(simplify_fraction(10,2))

    #problem 5
    print(correct_digits(1))

    #problem 6
    print(fraction_maker(22,96))







def power(x, n):
    if n == 0:
        return 1

    return x * power(x, n-1)

def interleave(L1, L2):
    if len(L1) == 0:
        return []
    return [L1[0], L2[0]] + (interleave(L1[1:], L2[1:]))

def reverse_rec(L):
    if len(L) <= 1:
        return L
    return [L[len(L)-1]] + reverse_rec(L[1:len(L)- 1]) +  [L[0]]

def zigzag1(L):
    if len(L) == 0:
        print("")
    elif len(L) == 1:
        print(L[0], end = "")
    else:
        print(L[0], L[-1], end = "")
        zigzag1(L[1:-1])

def floordivprint(L):
    if len(L) == 0:
        print("")
    elif len(L) == 1:
        print(L[0], end = "")
    else:
        print(L[len(L)//2], L[(len(L)//2) - 1], sep = " ", end = " ")
        floordivprint(L[0:(len(L)//2) - 1] + L[(len(L)//2)+1:])




def is_balanced(s):
    if "(" not in s:
        if ")" in s:
            return False
        return True

    first = s.find("(")
    print(first)
    if ")" not in s or s.find(")") < first:
        return False

    #Index values of closed brackets
    indicies = []
    for i in range(len(s)):
        if s[i] == ")":
            indicies.append(i)

    #iterate through index values of closed brackets
    for elem in indicies:
        if s[first:elem+1].count("(") == s[first:elem+1].count(")"):
            if elem == len(s):
                return is_balanced(s[first+1:-2:])
            else:
                return is_balanced(s[first+1:elem:]) and is_balanced(s[elem+1:])
    return False

    # if s[first+1::].find(")") < s[first+1::].find("("):
    #     new_start = s[first+1::].find(")")
    #     return is_balanced(s[new_start::])









if __name__ == "__main__":
    #1
    # print(power(5, 3))

    #2
    # L1 = [1, 2, 3, 4, 5]
    # L2 = [6, 7, 8, 9, 10]
    # print(interleave(L1, L2))

    #3
    # L3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # # print(reverse_rec(L3))
    #
    # #4
    # floordivprint(L3)

    #0, 1, 2, 3, 4, 5, 6, 7, 8, 9 10
    #5, 4, 6, 3

    #5
    s = "(()(()))"
    print(is_balanced(s))
    t = "(well (I think), recursion works like that (as far as I know))"
    print(is_balanced(t))



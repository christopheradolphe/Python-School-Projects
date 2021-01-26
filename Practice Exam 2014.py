def print_almost_all(L):
    for i in range(len(L)-1):
        print(L[i])

def h():
    global treat
    treat = "candy"

def all_not_same(a, b, c):
    if a == b and b == c:
        return False
    else:
        return True

def flatten(list_of_lists):
    result = []
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            result.append(list_of_lists[i][j])
    return result



if __name__ == "__main__":
    # list = [1, 2, 3, 4, 5]
    # print_almost_all(list)

    #1c
    #h()
    # treat = "pumpkin"
    # h()
    # print(treat)

    #2b
    # for i in range(-500, 501):
    #     print(i)

    # #2d
    # print(all_not_same(2, 2, 2))
    #
    # #4
    # L1 = [[1, 3], ['a', 'b', 'c']]
    # print(flatten(L1))

    #5
    # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # for s in letters:
    #     for t in letters:
    #         for q in letters:
    #             for r in letters:
    #                 allowed = True
    #                 four_letter_word = s + t + q + r
    #                 for i in range(len(four_letter_word)):
    #                     for j in range(1, len(four_letter_word)):
    #                         if four_letter_word[i] == four_letter_word[j]:
    #                             while j < 3:
    #                                 j+=1
    #                                 if four_letter_word[i] == four_letter_word[j]:
    #                                     allowed = False
    #                 if allowed:
    #                     print(four_letter_word)

    #Bonus






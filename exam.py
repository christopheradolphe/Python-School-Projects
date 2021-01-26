import numpy as np
#1
#We want to find the word that is the most frequent
#    word in the most files.
#make all lower case
def find_most_common_word(text):
    d = {}
    for word in text:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1
    occurences = list(d.values())
    max_occurences = max(occurences)
    for key in d.keys():
        if d[key] == max_occurences:
            return key
    return None



def most_common_frequent_word(files):
    most_frequent_words = {}
    for file in files:
        f = open(file)
        text = f.read().lower().replace("!", " ").replace("?", " ").replace(".", " ").replace("-", "  ").replace(",", "").replace("\n", " ").replace("  ", " ").split(" ")
        most_common_word = find_most_common_word(text)
        if most_common_word in most_frequent_words.keys():
            most_frequent_words[most_common_word] += 1
        else:
            most_frequent_words[most_common_word] = 1
    times_the_most_common = list(most_frequent_words.values())
    max_times = max(times_the_most_common)
    for key in most_frequent_words.keys():
        if most_frequent_words[key] == max_times:
            return key
    return None



#2
# need to isolate "<a href = "link">title</a>"
def get_links(html_text):

    d = {}
    start = 0
    for i in range(html_text.count("<a href")):
        start_value = html_text[start:].find("<a href")
        end_value = html_text[start:].find("</a>")
        link_title = html_text[start+start_value+11:start+end_value]
        second_greater_than_sign = link_title.find(">")
        link = link_title[:second_greater_than_sign-1]
        title = link_title[second_greater_than_sign+1:]
        d[title] = link
        start += end_value + 4
    return d



#3

def merge(L1, L2):
    while x < len(L1) + len(L2):       #Runtime complexity outer = 0(kn) where k is a constant
        i, j = 0, 0
        merged = []
        while i < len(L1) and j < len(L2):  #Runtime complexity inner = 0(jn)
            if L1[i] < L2[j]:
                merged.append(L1[i])
                i += 1
            else:
                merged.append(L2[j])
                j += 1

    merged.extend(lis1[i:])
    merged.extend(lis2[j:])

    return merged                                #Total runtime of merge = 0(n^2)





def merge_sort(L):
                                                #Runtime: runtime of merge * levels of merge_sort
                                                #Drawing at bottom to show work
                                                # levels = log2_n
                                                #Thus total run_time of merge_sort is:
                                                # runtime of merge     levels of merge_sort
                                                #       n^2          *        log2_n +1
                                                #Thus total runtime is n^2*log2_n +1
                                                #Getting rid of the constants we get
                                                # Runtime = (n^2)*(logn)
    #base case
    if len(L) <= 1:
        return L[:]

    mid = len(lis)//2
    return merge(merge_sort(lis[:mid]), merge_sort(lis[mid:]))
#
#
def f(n):
    #create a list in decreasing order
    array = np.random.rand(1, n)
    l = list(array)                              #Runtime to make list : tn where t is constant
    merge_sort(list)                             # or O(n)
    return None

#Therefore total runtime of function f(n): runtime f(n) + runtime merge_sort
 #                                         = 0(n) + 0(n^2*logn)
#                                           = 0(n^2 + )(n^2*logn)
#
    #Call tree of merge sort f(n)

    """
    [1]                                     [1]                 log2_n +1
      .                                   .
       .                                .
        .                             .
          [n/4]    [n/4] [n/4]     [n/4]                        3
            \      /       |     /
              [n/2]     [n/2]                                  2
                 \       /
                    [n]                                level: 1

Runtime per level is O(n^2) given all inputs are put into merge which has runtime of O(n^2) where h is a constant

"""


#4
def get_all_combinations(values, n, start_str = ""):
    '''Return a list of all possible values '''
    if n == 0:
        return [start_str]

    res = []
    for value in values:
        if str(value) not in start_str:
            res.extend(get_all_combinations(values, n-1, start_str + str(value)))
    return res

def get_target_noparens(nums, target):
    numcombos = get_all_combinations(nums, 3)
    # for elem in num:
    #     if len(elem) < 3:
    #         num.remove(elem)
    combinations_that_work = []
    for elem in numcombos:
        num1 = int(elem[0])
        num2 = int(elem[1])
        num3 = int(elem[2])
        if (num1 + num2 + num3) == target:
            combinations_that_work.append(str(num1) + "+" + str(num2) + "+" + str(num3))
        if (num1 + num2 * num3) == target:
            combinations_that_work.append(str(num1) + "+" + str(num2) + "*" + str(num3))
        if (num1 + num2 / num3) == target:
            combinations_that_work.append(str(num1) + "+" + str(num2) + "/" + str(num3))
        if (num1 + num2 - num3) == target:
            combinations_that_work.append(str(num1) + "+" + str(num2) + "-" + str(num3))


        if (num1 - num2 + num3) == target:
            combinations_that_work.append(str(num1) + "-" + str(num2) + "+" + str(num3))
        if (num1 - num2 * num3) == target:
            combinations_that_work.append(str(num1) + "-" + str(num2) + "*" + str(num3))
        if (num1 - num2 / num3) == target:
            combinations_that_work.append(str(num1) + "-" + str(num2) + "/" + str(num3))
        if (num1 - num2 - num3) == target:
            combinations_that_work.append(str(num1) + "-" + str(num2) + "-" + str(num3))

        if (num1 * num2 + num3) == target:
            combinations_that_work.append(str(num1) + "*" + str(num2) + "+" + str(num3))
        if (num1 * num2 - num3) == target:
            combinations_that_work.append(str(num1) + "*" + str(num2) + "-" + str(num3))
        if (num1 * num2 * num3) == target:
            combinations_that_work.append(str(num1) + "*" + str(num2) + "*" + str(num3))
        if (num1 * num2 / num3) == target:
            combinations_that_work.append(str(num1) + "*" + str(num2) + "/" + str(num3))

        if (num1 / num2 / num3) == target:
            combinations_that_work.append(str(num1) + "/" + str(num2) + "/" + str(num3))
        if (num1 / num2 + num3) == target:
            combinations_that_work.append(str(num1) + "/" + str(num2) + "+" + str(num3))
        if (num1 / num2 - num3) == target:
            combinations_that_work.append(str(num1) + "/" + str(num2) + "-" + str(num3))
        if (num1 / num2 * num3) == target:
            combinations_that_work.append(str(num1) + "/" + str(num2) + "*" + str(num3))
    return combinations_that_work[0]

#5
def get_target(nums, target):
    #all possible operations
    operations = ["+", "-", "*", "/"]
    #First find all permutations of numbers
    numcombos = get_all_combinations(nums, len(nums))
    #Create all permutations of the operations
    opcombos = get_all_combinations(operations,len(nums)-1)
    #Get all permutations of all number combinations with all operation combinations and check to see if any permutation is equal to target (This would be next step)
    for numbcombo in numcombos:
        for opcombo in opcombos:
            #this is section that needs to be worked on
            pass
    #if no combos work, return None
    return "7"     #this is to ensure string is returned from function

if __name__ == "__main__":
    #1
    #Punctuation
    #[".", ",", "!", "?", "-"]
    # print(most_common_frequent_word(["diseases/AIDS.html", "diseases/Bacteria.html", "diseases/Ebola.html"]))


    #2
    print(get_links('<a href =            "http://engsci.utoronto.ca">EngSci homepage2</a> my home is so nice i eat so much         cake <a href = "http://engsci.utoronto.ca">EngSci homepage</a> thank you for eating              my cake <a href = "http://ucc.on.ca">UCC page</a>'))

    #4
    # print(get_all_subsets([1, 2, 3]))

    # print(get_target_noparens([3, 1, 2], 7))

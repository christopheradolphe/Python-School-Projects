#Problem 1
def print_lol_lines(text):
    lines = text.split("\n")
    for elem in lines:
        elem_lc = elem.lower()
        if "lol" in elem_lc:
            print(elem)

#Problem 2
def dict_to_str(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other.
    For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".
    (the order of the key-value pairs doesn’t matter and can be different
    every time).
    """
    string = ""
    for key, value in d.items():
        string += str(key) + ", " + str(value) + "\n"
    return string

#Problem 3
def dict_to_str_sorted(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other, and are sorted in
    ascending order by key.
    For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
    return "0, 3\n1, 2\n10, 5". The keys in the string must be sorted
    in ascending order."""
    keys = []
    string = ""
    for key in d.keys():
        keys.append(key)
    keys.sort()
    for elem in keys:
        string += str(elem) + ", " + str(d[elem]) + "\n"
    return string




if __name__ == "__main__":
    # f = open("data2.txt")
    # text = f.read()
    # print_lol_lines(text)
    #
    # #Problem 2
    # d = {}
    # d[1] = 2
    # d[5] = 6
    # print(d)
    # print(dict_to_str(d))

    #Problem 3
    d = {}
    d[1] = 2
    d[0] = 3
    d[10] = 5
    print(d)
    print(dict_to_str_sorted(d))

    #Problem 4a
    f = open("phones.txt")
    text = f.read()
    lines = text.split("\n")
    d_phones = {}
    for elem in lines:
        if elem[0:2] != ";;":
            key_ind = elem.find("  ")
            key = elem[0:key_ind]
            value = elem[key_ind+2:].split(" ")
            d_phones[key] = value
    print(d_phones['AANCOR'])



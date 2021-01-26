#frequency = number of occurences / number of total words


def store(textfile):
    text = open(textfile, encoding="latin-1").read().split().replace(".", "").replace("!", "").lower()
    word_counts = {}
    for elem in text:
        if elem in word_counts:
            word_counts[elem] += 1
        else:
            word_counts[elem] = 1
    return word_counts

def top10(L):
    L.sort()
    length = len(L)
    return L[length - 10:]

def invertdict(dict):
    dict = {value:key for key, value in dict.items()}
    return dict

def tenmostfreq(text):
    word_counts = store(text)
    word_counts = invertdict(word_counts)
    word_counts = sorted(word_counts.items())
    topten = top10(word_counts)
    toptenvalues = []
    for elem in topten:
        toptenfreq, toptenvalue = elem
        toptenvalues.append(toptenvalue)
    print(toptenvalues)

def search_to_url(L):
    for i in range(len(L)):
        L[i] = L[i].replace(" ", "+")
    return L

def choosevariant(variants):
    search_to_url(variants)
    import urllib.request
    results = {}
    for elem in variants:
        f = urllib.request.urlopen("https://ca.search.yahoo.com/search;_ylt=Av3YHOEya_QRKgRTD8kMWgst17V_?p=" + elem +  "&amp;toggle=1&amp;cop=mss&amp;ei=UTF-8&amp;fr=yfp-t-715&amp;fp=1")
        page = f.read().decode("utf-8")
        f.close()
        # print(page)
        # word_counts = store(page)
        # word_counts = invertdict(word_counts)
        # word_counts = sorted(word_counts.items())




#1a


if __name__ == "__main__":
    #1a
    # word_counts = store("NotesfromUnderground.txt")
    # print(word_counts)
    # print(word_counts["sick"])

    #1b


    #1c
    inv_freq = {6: "the", 12: "a", 1:"hi"}
    print(sorted(inv_freq.items()))

    tenmostfreq("PrideandPrejudice.txt")

    #3
    # variants = ["fifth anniversary", "five year anniversary"]
    # choosevariant(variants)
    # choosevariant(variants)



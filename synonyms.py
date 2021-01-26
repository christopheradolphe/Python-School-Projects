import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    numerator = 0
    for key, value in vec1.items():
        if key in vec2.keys():
            numerator += vec1[key] * vec2[key]
    denominator = 0
    den_v1 = 0
    den_v2 = 0
    for key, value in vec1.items():
        den_v1 += value**2
    for key, value in vec2.items():
        den_v2 += value**2
    denominator = (den_v1*den_v2)**(1/2)
    similarity = numerator/denominator
    return similarity

def adding_words_to_dict(words):
    for i in range(len(sentence)):
        if sentence[i] not in d:
            d[sentence[i]] = {}
        for otherword in sentence:
            if otherword == word:
                pass
            else:
                if otherword in d[word]:
                    d[word][otherword] += 1
                else:
                    d[word][otherword] = 1

def removedoubleword(sentence):
    for word in sentence:
        if sentence.count(word) > 1:
            sentence.remove(word)

def build_semantic_descriptors(sentences):
    d = {}
    #print("Sentences:", sentences)
    for sentence in sentences:
        #print("Sentence:", sentence)
        for word in sentence:
            if len(word) == 0:
                sentence.remove(word)
        for word in sentence:
            if word not in d.keys():
                d[word] = {}
            for otherword in sentence:
                if otherword == word or otherword == '':
                    pass
                elif otherword in d[word].keys():
                    d[word][otherword] += 1
                else:
                    d[word][otherword] = 1
    return d

def update(d, sentences):
    new_d = build_semantic_descriptors(sentences)
    for key, values in new_d.items():
        if key in d.keys():
            for new_d_key, new_d_values in new_d[key].items():
                if new_d_key in d[key].keys():
                    d[key][new_d_key] += new_d[key][new_d_key]
                else:
                    d[key][new_d_key] = new_d[key][new_d_key]
        else:
            d[key] = new_d[key]
    return d

def build_semantic_descriptors_from_files(filenames):
    d = {}
    for i in range(len(filenames)):
        # print(filenames[i])
        f = open(filenames[i], encoding="latin-1")
        text = f.read().lower().replace("!", ".").replace("?", ".").replace("-", " ").replace("--", " ").replace(",", "").replace(":", "").replace(";", "").replace(". ", ".").replace(" .", ".").replace(". ", ".").replace("\n", " ").replace("  ", " ").split(".")
        sentences = []
        for elem in text:
            new_sentence = elem.split(" ")
            # print("new_sentece =", new_sentence)
            # print(type(new_sentence))
            length = len(new_sentence)
            i = 0
            while i < length:
                # print("New type is: ", type(new_sentence))
                if new_sentence.count(new_sentence[i]) > 1:
                    new_sentence.remove(new_sentence[i])
                    length -= 1
                else:
                    i += 1
            sentences.append(new_sentence)
        d = update(d, sentences)
    return d

def similarity_finder(word, choice, semantic_descriptors, similarity_fn):
    vec1 = semantic_descriptors[word]
    # print(vec1, "vec1")
    if choice in semantic_descriptors.keys():
        vec2 = semantic_descriptors[choice]
    else:
        vec2 = {-1: -1}
    # print(vec2, "vec2")
    similarity = similarity_fn(vec1, vec2)
    return similarity



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    similarities = []
    for elem in choices:
        similarities.append(similarity_finder(word, elem, semantic_descriptors, similarity_fn))
    max_value = max(similarities)
    index = similarities.index(max_value)
    return choices[index]



def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    f = open(filename, encoding="latin-1")
    questions = f.read().split("\n")
    for i in range(len(questions)):
        questions[i] = questions[i].split(" ")
    answers = []
    guesses = []
    #print("question:", questions)
    for question in questions:
        if len(question) > 2:
            answers.append(question[1])
            guesses.append(most_similar_word(question[0], question[2:], semantic_descriptors, similarity_fn))
        else:
            questions.remove(question)
    total = len(questions)
    #print(answers)
    #print(guesses)
    correct = 0
    for i in range(len(answers)):
        if answers[i] == guesses[i]:
            correct += 1
    #print(correct/total * 100)
    return (correct/total) * 100

if __name__ == "__main__":
    # print(norm({"a": 1, "b": 2, "c": 3}))

    #print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))

    # sentences = [["i", "am", "a", "sick", "man"],
    # ["i", "am", "a", "spiteful", "man"],
    # ["i", "am", "an", "unattractive", "man"],
    # ["i", "believe", "my", "liver", "is", "diseased"],
    # ["however", "i", "know", "nothing", "at", "all", "about", "my",
    # "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
    # print(build_semantic_descriptors(sentences))


    #3

    # sem_descriptors = build_semantic_descriptors_from_files(["WarandPeace.txt", "Swann'sWay.txt"])
    #
    # #4
    # # q = ["i", "j", "k"]
    # # l = [2, 3, 5]
    # # m = max(l)
    # # index = l.index(m)
    # #
    # # print(q[index])
    # #
    # # #5
    # # run_similarity_test("Project3Example.txt", semantic_descriptors, cosine_similarity)
    # res = run_similarity_test("Project3Example.txt", sem_descriptors, cosine_similarity)
    # print(res, "of the guesses were correct")
    # vec1 = {'cat': 1, 'food': 1}
    # vec2 = {'dog': 1}
    #
    # list = [-1, 0, 0, 0]
    # print(max(list))
    # index = list.index(0)
    # print(index)

    sem_desc = {"dog": {"cat": 1, "food": 1},
                        "cat": {"dog": 1}}
    print(most_similar_word("dog", ["cat", "rat"], sem_desc, cosine_similarity))

    build_semantic_descriptors_from_files(["Project3Example.txt"])


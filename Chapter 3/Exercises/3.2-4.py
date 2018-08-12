words = ["Hello", "my", "same", "is", "Anthony", "Okayy", "Heyyy"]


def count_words():
    count = 0
    for word in words:
        if word.count(str()) == 6:
            count +=1
            print(word, "is 5 str long.")
    print(count, "words with 5 in length.")


count_words()
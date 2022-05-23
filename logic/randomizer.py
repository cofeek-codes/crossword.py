import random


def randomize_words(current_words):
    randomized_words = []
    for word in range(0, int((len(current_words) / 100 * 80))):
        word = random.choice(current_words)
        randomized_words.append(word)
    print(randomized_words)
    print(len(randomized_words))
    print(len(current_words))
    # return randomized_words


# per to variable
# less check

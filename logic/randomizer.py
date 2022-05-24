import random


def randomize_words(current_words):
    per = len(current_words) / 100 * 80
    randomized_words = []
    for word in range(0, int(per)):
        word = random.choice(current_words)
        randomized_words.append(word)
    return randomized_words


# less check

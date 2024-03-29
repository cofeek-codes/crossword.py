import random
from pywebio.output import *
from pywebio.input import *
from tabulate import tabulate


def input_web(randomized_words, chosen_theme):
    put_markdown(f'тема: {chosen_theme}')
    input_table(randomized_words)


def input_table(randomized_words):
    words = randomized_words
    for word in words:

        for letter in word:
            if (word.index(letter) + 1) < len(word):
                next_letter = word[word.index(letter) + 1]
                random_letter = random.choice(word)

        put_grid([
            [put_text(random_letter), put_text(random_letter),
                 put_text(random_letter), put_text(random_letter), put_text(random_letter), put_text(random_letter)],
            [put_text(random_letter), put_text(
                random_letter), put_text(random_letter), put_text(random_letter), put_text(random_letter), put_text(random_letter)],
        ], cell_width='70px', cell_height='70px').style('font-size:18px; font-weight:bold;')
        random_letter = random.choice(word)

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

        put_grid([
            [put_text(letter), put_text(next_letter),
                 put_text(letter), put_text(letter), put_text(letter), put_text(letter)],
            [put_text(next_letter), put_text(
                next_letter), put_text(letter), put_text(letter), put_text(letter), put_text(letter)],
        ], cell_width='70px', cell_height='70px').style('font-size:18px; font-weight:bold;')
        next_letter = int(word.index(next_letter)) + 1

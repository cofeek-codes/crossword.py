import random
from pywebio.output import *
from pywebio.input import *
from tabulate import tabulate


def input_web(randomized_words, chosen_theme):
    put_markdown(f'тема: {chosen_theme}')
    input_table(randomized_words)


def input_table(randomized_words):
    words = randomized_words
    all_letters = []
    for word in words:
        for letter in word:
            all_letters.append(letter)
        for letter in all_letters:

            put_grid([
                [put_text(letter), put_text(letter),
                    put_text(letter), put_text(letter), put_text(letter), put_text(letter)],
                [put_text(letter), put_text(
                    letter), put_text(letter), put_text(letter), put_text(letter), put_text(letter)],
            ], cell_width='70px', cell_height='70px').style('font-size:18px; font-weight:bold;')

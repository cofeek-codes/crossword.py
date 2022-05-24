from pywebio.output import *
from pywebio.input import *


def input_web(randomized_words, chosen_theme):
    put_markdown(f'тема: {chosen_theme}')
    for word in randomized_words:
        put_markdown(word)

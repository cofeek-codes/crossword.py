from itertools import count
import os
import re
from pywebio.output import *
from pywebio.output import *

from logic.get_themes import get_themes
from logic.randomizer import randomize_words


def get_words(theme):
    theme_words_file = open(f'themes/{theme}/{theme}.txt', 'r')
    words_ff = theme_words_file.read()
    theme_words_file.close()
    words = words_ff.split('\n')
    return words


chosen_theme = input('выбирете тему ')


def main():
    themes = init_themes()

    if chosen_theme not in themes:
        print('Выбраной темы не существует')
    else:
        theme_words = get_words(chosen_theme)
        if themes.index(chosen_theme) >= 2:
            # prev
            # second backward theme
            theme_back_twice = themes[(themes.index(chosen_theme)) - 2]
            theme_back_twice = get_words(theme_back_twice)
            # first backward theme
            theme_back_once = themes[(themes.index(chosen_theme)) - 1]
            theme_back_once = get_words(theme_back_once)
            current_words = theme_words + theme_back_once + theme_back_twice

        elif themes.index(chosen_theme) >= 1:

            prev = themes[(themes.index(chosen_theme)) - 1]
            prev = get_words(prev)
            current_words = theme_words + prev
        else:
            current_words = theme_words
            # empty string check
        if '' in current_words:
            current_words.remove('')
        # print(current_words)
        randomized_words = randomize_words(current_words)
        print(randomized_words)
        print(len(randomized_words))
    # randomize words


def init_themes():
    themes_storage = open('themes/themes.txt')
    themes = get_themes(themes_storage)
    themes_storage.close()
    for theme in themes:
        if os.path.exists(f'themes/{theme}') == False:
            os.mkdir(f'themes/{theme}')
            theme_words = open(f'themes/{theme}/{theme}.txt', 'w')
            theme_words.close()
            print(f'Заполните тему {theme}')
    return themes


if __name__ == '__main__':
    main()

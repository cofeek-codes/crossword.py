import os
from pywebio.output import *
from pywebio.output import *

from logic.get_themes import get_themes


def get_words(theme):
    theme_words_file = open(f'themes/{theme}/{theme}.txt', 'r')
    words_ff = theme_words_file.read()
    theme_words_file.close()
    words = words_ff.split('\n')
    return words


chosen_theme = input('выбирете тему ')


def main():
    themes = init_themes()
    theme_words = get_words(chosen_theme)
    if chosen_theme not in themes:
        print('Выбраной темы не существует')
    else:
        if themes.index(chosen_theme) >= 2:
            # prev
            prev = themes[(themes.index(chosen_theme)) - 2]
            prev = get_words(prev)
            current_words = theme_words + prev

            # print(prev)
        elif themes.index(chosen_theme) >= 1:

            prev = themes[(themes.index(chosen_theme)) - 1]
            prev = get_words(prev)
            current_words = theme_words + prev
        else:
            current_words = theme_words

        print(current_words)
    # get_current theme and prev
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
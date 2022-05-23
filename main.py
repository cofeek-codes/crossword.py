import os
from pywebio.output import *
from pywebio.output import *

from logic.get_themes import get_themes


def get_words(theme):
    theme_words_file = open(f'themes/{theme}/{theme}.txt', 'r')
    words = theme_words_file.read()
    theme_words_file.close()
    words = words.split('\n')
    return words


chosen_theme = input('выбирете тему ')


def main():
    themes = init_themes()
    if chosen_theme not in themes:
        print('Выбраной темы не существует')
    else:
        theme_words = get_words(chosen_theme)
        print(theme_words)
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

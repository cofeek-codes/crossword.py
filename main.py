from pywebio.output import *
from pywebio.output import *

from logic.get_themes import get_themes


def get_words(theme):
    theme_words_file = open(f'themes/{theme}/{theme}.txt')
    words = theme_words_file.read()
    theme_words_file.close()
    words = words.split('\n')
    # print(words)
    return words


def main():
    themes_storage = open('themes/themes.txt')
    themes = get_themes(themes_storage)
    themes_storage.close()

    current_theme_words = get_words(themes[0])
    print(current_theme_words)


# for theme in themes:
#     pass


if __name__ == '__main__':
    main()

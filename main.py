import os
from pywebio.output import *
from pywebio.output import *

from logic.get_themes import get_themes


def main():
    themes_storage = open('themes/themes.txt')
    themes = get_themes(themes_storage)
    themes_storage.close()

    for theme in themes:
        if os.path.exists(f'themes/{theme}') == False:
            os.mkdir(f'themes/{theme}')
            words_storage = open(f'themes/{theme}/{theme}.txt', 'w')
            words_storage.close()
            words_storage = open(f'themes/{theme}/{theme}.txt', 'w')
            words = words_storage.read()
            words_storage.close()

        else:
            words_storage = open(f'themes/{theme}/{theme}.txt', 'w')
            words_storage.close()
            words_storage = open(f'themes/{theme}/{theme}.txt', 'r')
            words = words_storage.read()
            words_storage.close()

        print(words)


if __name__ == '__main__':
    main()

from pywebio.output import *
from pywebio.output import *

from logic.get_themes import get_themes


def main():
    themes_storage = open('themes/themes.txt')
    themes = get_themes(themes_storage)
    themes_storage.close()

    for theme in themes:
        pass


if __name__ == '__main__':
    main()

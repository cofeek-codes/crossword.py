def get_themes(themes_storage):
    # get themes
    themes = themes_storage.read()
    themes = themes.split('\n')
    # print(themes)
    return themes

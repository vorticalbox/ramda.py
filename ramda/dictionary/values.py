from ramda.function.curry import curry


@curry
def values(dict):
    return dict.values()

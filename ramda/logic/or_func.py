from ramda.function.curry import curry


@curry
def or_func(a, b):
    return a or b

from ramda.function.curry import curry


@curry
def identical(x, y):
    return x is y

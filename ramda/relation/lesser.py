from ramda.function.curry import curry


@curry
def lesser(a, b):
    return a if a <= b else b

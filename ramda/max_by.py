from ramda.curry import curry


@curry
def max_by(f, x, y):
    return x if f(x) > f(y) else y

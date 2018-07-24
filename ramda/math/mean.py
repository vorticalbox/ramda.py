from ramda.function.curry import curry


@curry
def mean(xs):
    return sum(xs) / len(xs)

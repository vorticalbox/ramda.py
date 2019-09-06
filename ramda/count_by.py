from toolz import curry
from collections import Counter


@curry
def count_by(function, list):
    """Counts the elements of a list according to how many match each value of a
key generated by the supplied function. Returns an object mapping the keys
produced by fn to the number of occurrences in the list. Note that all
keys are coerced to strings because of how JavaScript objects work.
Acts as a transducer if a transformer is given in list position"""
    count = Counter()

    for x in list:
        count[function(x)] += 1

    return dict(count)

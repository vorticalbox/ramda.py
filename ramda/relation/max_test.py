from .max import max
from ramda.private.asserts import assert_equal


def max_test():
    assert_equal(max([1, 3, 4, 2]), 4)

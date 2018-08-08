from ramda.private.asserts import *
from ramda.cond import cond
from ramda.always import always
from ramda.equals import equals


def nothing(temp):
    return 'nothing special happens at ' + str(temp) + '°C'


f = cond([
    (equals(0), always('water freezes at 0°C')),
    (equals(100), always('water boils at 100°C')),
    (always(True), nothing)
])


def cond_test():
    assert_equal(f(0), 'water freezes at 0°C')
    assert_equal(f(100), 'water boils at 100°C')
    assert_equal(f(50), 'nothing special happens at 50°C')
    assert_equal(cond([], 10), None)

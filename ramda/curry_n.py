from toolz import curry
from ramda.n_ary import n_ary


@curry
def curry_n(n, f):
    """Returns a curried equivalent of the provided function, with the specified
arity. The curried function has two unusual capabilities. First, its
arguments needn't be provided one at a time. If g is R.curryN(3, f), the
following are equivalent:
g(1)(2)(3)
g(1)(2, 3)
g(1, 2)(3)
g(1, 2, 3)
Secondly, the special placeholder value R.__ may be used to specify
"gaps", allowing partial application of any combination of arguments,
regardless of their positions. If g is as above and _ is R.__,
the following are equivalent:
g(1, 2, 3)
g(_, 2, 3)(1)
g(_, _, 3)(1)(2)
g(_, _, 3)(1, 2)
g(_, 2)(1)(3)
g(_, 2)(1, 3)
g(_, 2)(_, 3)(1)"""
    return curry(n_ary(n, f))

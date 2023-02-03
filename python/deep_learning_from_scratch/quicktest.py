import numpy as np
from numpy import *
from typing import Callable

def deriv(func: Callable[[ndarray], ndarray],
        input_: ndarray,
        delta: float = 0.001) ->ndarray:
        '''Evaluates the derivative of a function "func" at every element in the "input_" array.'''
        return (func(input_ + delta) - func(input_ - delta)) / (2 * delta)


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
deriv(a)

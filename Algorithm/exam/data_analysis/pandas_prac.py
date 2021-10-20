import numpy as np
import pandas as pd
from pandas import DataFrame, Series

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.array([1, 2, 3])
print(a, b)

a = np.random.rand(12).reshape(3, 4)
print(a)

a = np.random.randint(1, 10, 9)
print(a)

a = np.random.randn(10)
print(a)

a = np.zeros(10).reshape(2, 5)
print(a)

a = np.ones(10).reshape(2, 5)
print(a)

print(np.arange(3, 12).reshape(3, 3))

print(np.full((5, 5), 0))




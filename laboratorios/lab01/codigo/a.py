import numpy as np
from collections import deque


a = deque([1,2,3])

while a:
    print(a.pop())
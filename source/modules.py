# Import entire module
import math

print(math.sqrt(16))
print(math.pi)

# Import specific names
from math import sqrt, pi

print(sqrt(9))
print(pi)

# Import with alias
import math as m

print(m.floor(3.7))

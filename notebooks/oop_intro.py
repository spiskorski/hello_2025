# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Introduction to object oriented programming in Python

# %% [markdown]
# **Task** Implement  a class `ComplexNumber` describing complex numbers. It should have methods `__add__` (addition), `__mul__` (multiplication), `__abs__` (module of the complex number), _n_-th root

# %%
# %load_ext nb_mypy

# %%
import math
class ComplexNumber:
    def __init__(self, re: float, im: float):
        self.re = re
        self.im = im
        
    def __repr__(self):
        if self.im < 0:
            return f"{self.re} - {-self.im}i"
        else:
            return f"{self.re} + {self.im}i"
        
    def __add__(self, other: ComplexNumber) -> ComplexNumber:
        if not isinstance(other, ComplexNumber):
            raise ValueError("The second argument should be complex number")
        
        return ComplexNumber(self.re + other.re, self.im + other.im)
        #return 7

    def __mul__(self, other: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __abs__(self) -> float:
        return math.sqrt(self.re ** 2 + self.im ** 2)

    def radius(self):
        pass

    @property
    def angle(self):
        return math.atan2(self.im, self.re)
    
    def nth_root(self, n):
        roots = []
        r = abs(self)

        #if x == 0 and y == 0:
            #theta = 0
        #else:
            #theta = 2 * math.atan( y / (math.sqrt(x**2 + y**2) + x) )

        theta = self.angle
        
        root_r = r ** (1/n)

        for k in range(n):
            angle = (theta + 2 * math.pi * k) / n
            re = root_r * math.cos(angle)
            im = root_r * math.sin(angle)
            roots.append(ComplexNumber(re, im))

        return roots

a = ComplexNumber(1, -1)
b = ComplexNumber(2, 4)

# %%
print(a * b)
print(a + b)
print(abs(a))
print(a.nth_root(2))

# %%
a + "hnjhf"

# %%
a.angle

# %%
a.re = 0

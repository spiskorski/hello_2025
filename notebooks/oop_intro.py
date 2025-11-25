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

# %% jupyter={"outputs_hidden": true}
# %load_ext nb_mypy

# %%
import math


# %%
class ComplexNumber:
    def __init__(self, re: float, im: float):
        self.re = re
        self.im = im
        
    def __repr__(self):
        if self.im < 0:
            return f"{self.re} - {-self.im}i"
        else:
            return f"{self.re} + {self.im}i"
        
    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        if not isinstance(other, ComplexNumber):
            raise ValueError("The second argument should be complex number")

        return type(self)(self.re + other.re, self.im + other.im)
        #return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __abs__(self) -> float:
        return math.sqrt(self.re ** 2 + self.im ** 2)

    def radius(self):
        pass

    @property
    def angle(self):
        return math.atan2(self.im, self.re)
    
    def nth_root(self, n) -> list:
        roots = []
        r = abs(self)

        #if x == 0 and y == 0:
            #theta = 0
        #else:
            #theta = 2 * math.atan( y / (math.sqrt(x**2 + y**2) + x) )
        theta = self.angle
        starting_angle = theta / n
        root_r = r ** (1/n)
        angels = [starting_angle + 2 * math.pi * k / n for k in range(n)]
        roots = [ComplexNumber(root_r * math.cos(angle), root_r * math.sin(angle)) for angle in angels]
        return roots


# %%
class RealNumber(ComplexNumber):
    
    def __init__(self, value: float, im = 0):
        super().__init__(re = value, im = 0)

    def __add__():
        pass


# %%
x1 = RealNumber(3)

# %%
x2 = RealNumber(4)

# %%
type(x1 + x2)

# %%
RealNumber(-3).angle

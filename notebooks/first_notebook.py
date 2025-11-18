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
# # My first notebook

# %% [markdown]
# ## Type annotations

# %% [markdown]
# The python language 

# %%
# %load_ext nb_mypy

# %%
name : str
age : int

# %%
name = "Jan"


# %%
# #!python -m pip install nb_mypy

# %% [markdown]
# # Annotating functions

# %%
def factorial(n : int) -> int:
    if n > 0 :
        return factorial(n-1) * n

    return 1


# %%
factorial(2)

# %%
factorial("Hello")

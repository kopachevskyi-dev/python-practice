"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the elements at odd indices (1, 3, 5, ...).
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = print([var for index, var in enumerate(a) if index % 2 != 0])

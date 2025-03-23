#https://cs50.harvard.edu/python/2022/psets/8/jar/


class Jar:
    """
    A class to represent a jar of cookies.

    Attributes:
        capacity (int): Maximum number of cookies the jar can hold.
        size (int): Current number of cookies in the jar.
    """

    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")



    def __str__(self):
        cookies = "🍪" * self.size
        return cookies


    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Adding too many cookies!")
        self._size += n


    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Taking too many cookies!")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

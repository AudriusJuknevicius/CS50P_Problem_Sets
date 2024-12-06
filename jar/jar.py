#https://cs50.harvard.edu/python/2022/psets/8/jar/

from jar import Jar


class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        if self.size != 0:
            cookies = "🍪" * self.size
        return cookies

    def deposit(self, n):
        if n + self._capacity >= 12
            raise ValueError("Too many cookies!")
        self._size = n + self._size


    def withdraw(self, n):
        if self._capacity - n < 0
            raise ValueError("No cookies left!")
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

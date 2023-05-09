# დავალება #37 - Cookie Jar

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError ("Not enough space in jar")
        else:
            self.size = self.size + n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError ("Not enough cookies in jar")
        else:
            self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError ("Wrong input")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Not enough cookies in jar")
        self._size = size
    

# jar = Jar()
# jar.deposit(5)
# jar.withdraw(2)
# print(jar)
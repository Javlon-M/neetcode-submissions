class MyHashSet:

    def __init__(self):
        self.hash = [-1] * 1000001
        
    def add(self, key: int) -> None:
        self.hash[key] = key

    def remove(self, key: int) -> None:
        self.hash[key] = -1

    def contains(self, key: int) -> bool:
        return self.hash[key] != -1
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.store[key]) - 1
        value = ""
        while l <= r:
            m = (l + r) // 2
            (val, time) = self.store[key][m]

            if time <= timestamp:
                value = val
                l = m + 1
            else:
                r = m - 1
            
        return value
            
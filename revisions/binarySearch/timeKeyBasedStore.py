class TimeMap:
    def __init__(self):
        self.store = {}  # key [value,timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        if key not in self.store:
            return res

        # O(logn)
        values = self.store[key]

        l, r = 0, len(values) - 1

        while l <= r:

            mid = (l + r) // 2

            if values[mid][1] == timestamp:
                return values[mid][0]

            # value is just right lets increase it
            if values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            else:  # too small
                r = mid - 1

        return res

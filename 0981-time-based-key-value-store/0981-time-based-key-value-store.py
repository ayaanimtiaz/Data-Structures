class TimeMap:
    # its likely
    # save key
    # store value and timestamp in a tuple
    # nested tuple inside of a bigger tuple
    # do binary search to find timestamp
    # l < r
    # probably a gimmickly binary search at th eend

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.time_map.get(key, 0) == 0:
            self.time_map[key] = [(timestamp, value)]
        else:
            self.time_map[key].append((timestamp, value))
    
        

    def get(self, key: str, timestamp: int) -> str:
        if self.time_map.get(key, 0) == 0:
            return ''

        left = 0
        right = len(self.time_map[key]) - 1
        middle = (left + right) // 2

        while left <= right:
            middle = (left + right) // 2

            if self.time_map[key][middle][0] == timestamp:
                return self.time_map[key][middle][1]
            elif self.time_map[key][middle][0] > timestamp:
                right = middle - 1
            else:
                left = middle + 1

        if self.time_map[key][right][0] > timestamp:
            return ''
        return self.time_map[key][right][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
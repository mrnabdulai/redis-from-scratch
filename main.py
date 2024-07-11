class RedisStore:

    def __init__(self):
        #values are lists of tuples (value, timestamp)
        self.hash_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.hash_map:
            value = self.hash_map[key]
            #try to find timestamped value with binary serch:
            l,r=0, len(value)-1
            while l <= r:
                m = (l +r)//2
                if value[m][1] == timestamp:
                    return value[m][0]

                elif timestamp > value[m][1] :
                    l = m + 1
                else:
                    r = m -1
            #if not find next least value
            for i in range(len(value)-1, -1, -1):
                if value[i][1] < timestamp:
                    return value[i][0]
            #if nothing found then return empty string
            return ""
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

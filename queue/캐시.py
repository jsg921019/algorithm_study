# https://programmers.co.kr/learn/courses/30/lessons/17680

# solution 1

def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time


# solution 2

from collections import deque

def solution2(cacheSize, cities):
    
    t = 0
    dq = deque()
    cache = dict()
    
    for city in [c.lower() for c in cities]:
        if city in cache:
            t += 1
            dq.append(city)
            cache[city] += 1
        else:
            t += 5
            dq.append(city)
            cache[city] = 1
            while len(cache) > cacheSize:
                c = dq.popleft()
                if cache[c] > 1:
                    cache[c] -= 1
                else:
                    del cache[c]
    return t


import random
import time

n = 10000
cities = [str(random.randint(0,100000)) for _ in range(200000)]

t0 = time.time()
solution(n, cities)
print(time.time() - t0)

t0 = time.time()
solution2(n, cities)
print(time.time() - t0)
def solution(cacheSize, cities):
    cache = []
    time = 0

# cacheSize가 0일 때 만약 cities에 ["LA", "LA"]가 있는 경우에 캐시를 저장하여 10이 아닌 6이 되기 때문에
# 캐시사이즈가 0이면 캐시를 저장하지 않도록 처리해줘야함.

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            time += 1
        else :
            if cache and len(cache) >= cacheSize:
                cache.pop(0)
            time += 5
        if cacheSize != 0: cache.append(city)

    return time
        

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

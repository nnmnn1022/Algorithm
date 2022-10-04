import time
start = time.time()

def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)):
        if i+1 < len(phone_book) and phone_book[i+1].startswith(phone_book[i]):
                return False

    return True

print(solution(["119", "97674223", "1195524421"]))
print("time :", time.time() - start)
print(solution(["123","456","789"]))
print("time :", time.time() - start)
print(solution(["12","123","1235","567","88"]))
print("time :", time.time() - start)
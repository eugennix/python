def rec():
    n = int(input())
    if n:
        return n + rec()
    return 0


print(rec())

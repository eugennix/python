''' https://www.coursera.org
/learn/python-osnovy-programmirovaniya/programming/XWi6G/sozdaniie-arkhiva
'''
free_space, n_users = map(int, input().split())
user_requests = sorted([int(input()) for _ in range(n_users)])
users_count = 0
for user_need_space in user_requests:
    if user_need_space <= free_space:
        free_space -= user_need_space
        users_count += 1
print(users_count)

# a, b = [''.join(sorted(input().lower())) for _ in range(2)]
# print(a == b)

def get_int(start_message, error_message, end_message) -> int:
    print(start_message)
    while True:
        try:
            s = input()
            n = int(s)
            print(end_message)
            return n
        except ValueError:
            print(error_message)

get_int('Hello', 'Error', 'Good buy!')

'''
def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        x = input()
        try:
            x = int(x)
        except ValueError:
            print(error_message)
        else:
            print(end_message)
            return x
'''
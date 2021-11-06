from test import Test


def sum_digits_in_range(n):
    if n <= 0: return 0
    ret = 45
    prev = 45
    n = (10**n)
    n = str(n)
    print(n)
    for i in range(2,len(n)):
        ret += ((45*i)*9)+(45*(i-1))
        
    return ret

print(sum_digits_in_range(3))
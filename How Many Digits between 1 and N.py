from test import Test

def digits(number):
    number = str(number)
    if len(number) == 1:
        return int(number)-1
    last = 1
    cnt = 0
    for i in range(1,len(number)):
        tmp1 = int('1'+'0'*(i))
        cnt += (((tmp1 - last)*(i)) + ((int(number[:i+1])-tmp1)*(i+1)))
        last = int(number[:i+1])
        print(cnt)
    return cnt

print(digits(252))
# Test.assert_equals(digits(1), 0)
# Test.assert_equals(digits(10), 9)
# Test.assert_equals(digits(100), 189)
# Test.assert_equals(digits(2020), 6969)
# Test.assert_equals(digits(103496754), 820359675)
# Test.assert_equals(digits(3248979384), 31378682729)
# Test.assert_equals(digits(122398758003456), 1724870258940729)
# Test.assert_equals(digits(58473029386609125789), 1158349476621071404669)
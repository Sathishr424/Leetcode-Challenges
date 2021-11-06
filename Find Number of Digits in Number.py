from test import Test

def num_of_digits(num):
    cnt = 1
    i = 10
    while i <= abs(num):
        cnt+=1
        i*=10
    return cnt

# print(num_of_digits(-12381428))
Test.assert_equals(num_of_digits(13124), 5)
Test.assert_equals(num_of_digits(0), 1)
Test.assert_equals(num_of_digits(-12381428), 8)
Test.assert_equals(num_of_digits(12), 2)
Test.assert_equals(num_of_digits(42), 2)
Test.assert_equals(num_of_digits(1000), 4)
Test.assert_equals(num_of_digits(136), 3)
Test.assert_equals(num_of_digits(1000000000), 10)
Test.assert_equals(num_of_digits(2147483647), 10)
Test.assert_equals(num_of_digits(-2147483647), 10)
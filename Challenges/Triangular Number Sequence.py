from test import test

def triangle(n):
	ret = 0
	for i in range(n):
		ret+=i+1
	return ret

Test = test()
Test.assert_equals(triangle(1), 1)
Test.assert_equals(triangle(2), 3)
Test.assert_equals(triangle(3), 6)
Test.assert_equals(triangle(8), 36)
Test.assert_equals(triangle(2153), 2318781)
		
		

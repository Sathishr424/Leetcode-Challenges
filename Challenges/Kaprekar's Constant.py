from test import Test

def recursion(val):
	if val == 6174: return 0
	if len(str(val)) < 4: val = str(val) + '0'
	num1 = list(str(val))
	num2 = list(str(val))
	num1.sort()
	num2.sort(reverse=True)
	num1 = int(''.join(num1))
	num2 = int(''.join(num2))
	return max(num2,num1) - min(num2,num1)

def kaprekar(num):
	ret = 0
	while num != 0:
		num = recursion(num)
		ret+=1
	return ret-1

Test.assert_equals(kaprekar(3524), 3)
Test.assert_equals(kaprekar(1112), 5)
Test.assert_equals(kaprekar(1342), 3)
Test.assert_equals(kaprekar(2636), 3)
Test.assert_equals(kaprekar(3219), 3)
Test.assert_equals(kaprekar(3305), 6)
Test.assert_equals(kaprekar(4132), 3)
Test.assert_equals(kaprekar(4568), 7)
Test.assert_equals(kaprekar(5610), 4)
Test.assert_equals(kaprekar(6002), 1)
Test.assert_equals(kaprekar(6081), 7)
Test.assert_equals(kaprekar(6174), 0)
Test.assert_equals(kaprekar(6287), 7)
Test.assert_equals(kaprekar(7093), 7)
Test.assert_equals(kaprekar(7412), 1)
Test.assert_equals(kaprekar(7735), 2)
Test.assert_equals(kaprekar(8591), 5)
Test.assert_equals(kaprekar(8621), 3)
Test.assert_equals(kaprekar(8650), 3)
Test.assert_equals(kaprekar(9618), 6)

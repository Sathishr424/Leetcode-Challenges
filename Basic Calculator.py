from test import Test

def calculator(num1, operator, num2):
	if operator == '+': return num1 + num2
	elif operator == '-': return num1 - num2
	elif operator == '*': return num1 * num2
	elif operator == '/':
		if num2 == 0:
			return "Can't divide by 0!"
		return num1 / num2

Test.assert_equals(calculator(2, '/', 2), 1)
Test.assert_equals(calculator(10, '-', 7), 3)
Test.assert_equals(calculator(2, '*', 16), 32)
Test.assert_equals(calculator(2, '-', 2), 0)
Test.assert_equals(calculator(15, '+', 26), 41)
Test.assert_equals(calculator(2, '+', 2), 4)
Test.assert_equals(calculator(2, "/", 0), "Can't divide by 0!")

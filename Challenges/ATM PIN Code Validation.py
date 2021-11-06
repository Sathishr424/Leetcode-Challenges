from test import Test

def is_valid_PIN(pin):
	if len(pin) != 4 and len(pin) != 6:
		return False
	for i in pin:
		if not i.isdigit(): return False
	return True
	
Test.assert_equals(is_valid_PIN("1234"), True)
Test.assert_equals(is_valid_PIN("12345"), False)
Test.assert_equals(is_valid_PIN("a234"), False)
Test.assert_equals(is_valid_PIN(""), False)
Test.assert_equals(is_valid_PIN("%234"), False)
Test.assert_equals(is_valid_PIN("`234"), False)
Test.assert_equals(is_valid_PIN("@234"), False)
Test.assert_equals(is_valid_PIN("#234"), False)
Test.assert_equals(is_valid_PIN("$234"), False)
Test.assert_equals(is_valid_PIN("*234"), False)
Test.assert_equals(is_valid_PIN("5678"), True)
Test.assert_equals(is_valid_PIN("^234"), False)
Test.assert_equals(is_valid_PIN("(234"), False)
Test.assert_equals(is_valid_PIN(")234"), False)
Test.assert_equals(is_valid_PIN("123456"), True)
Test.assert_equals(is_valid_PIN("-234"), False)
Test.assert_equals(is_valid_PIN("_234"), False)
Test.assert_equals(is_valid_PIN("+234"), False)
Test.assert_equals(is_valid_PIN("=234"), False)
Test.assert_equals(is_valid_PIN("?234"), False)

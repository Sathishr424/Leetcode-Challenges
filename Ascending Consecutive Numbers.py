from test import Test

def check(x, l):
	for i in range(0,len(x)-l,l):
		if int(x[i:i+l]) != int(x[i+l:i+(l*2)])-1: return False
	return True

def ascending(txt):
	l = 1
	while l <= len(txt)/2:
		if check(txt,l): return True
		l+=1
	return False
		
Test.assert_equals(ascending("232425"), True)
Test.assert_equals(ascending("444445"), True)
Test.assert_equals(ascending("1234567"), True)
Test.assert_equals(ascending("123412351236"), True)
Test.assert_equals(ascending("57585960616263"), True)
Test.assert_equals(ascending("500001500002500003"), True)
Test.assert_equals(ascending("919920921"), True)

Test.assert_equals(ascending("2324256"), False)
Test.assert_equals(ascending("1235"), False)
Test.assert_equals(ascending("121316"), False)
Test.assert_equals(ascending("12131213"), False)
Test.assert_equals(ascending("54321"), False)
Test.assert_equals(ascending("56555453"), False)
Test.assert_equals(ascending("90090190290"), False)
Test.assert_equals(ascending("35236237238"), False)


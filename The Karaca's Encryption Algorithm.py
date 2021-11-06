from test import Test

def checkIf(vov, val):
	for i in range(len(vov)):
		if vov[i] == val:
			return i
	return -1

def encrypt(word):
	rev = word[::-1]
	vov = 'aeou'
	vovNum = '0123'
	for i in range(len(rev)):
		tmp = checkIf(vov, rev[i])
		if tmp != -1:
			rev = rev.replace(rev[i], vovNum[tmp])
	return rev + "aca"
	
Test.assert_equals(encrypt("karaca"), "0c0r0kaca")
Test.assert_equals(encrypt("burak"), "k0r3baca")
Test.assert_equals(encrypt("banana"), "0n0n0baca")
Test.assert_equals(encrypt("alpaca"), "0c0pl0aca")
Test.assert_equals(encrypt("hello"), "2ll1haca")
			
			

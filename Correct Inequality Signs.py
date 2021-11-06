from test import Test

def checkCase(x,y,c):
	if c=='>':
		if x > y: return True
		return False
	elif c=='<':
		if x < y: return True
		return False

def correct_signs(txt):
	num = 0
	char = 'n'
	tmp = ''
	txt = txt.replace(' ','')
	for i in txt:
		if i=='<': 
			if char == 'n': 
				num = int(tmp)
				tmp = ''
			else:
				if not checkCase(num, int(tmp), char): return False
				num = int(tmp)
				tmp = ''
			char = '<'
		elif i=='>':
			if char == 'n': 
				num = int(tmp)
				tmp = ''
			else:
				if not checkCase(num, int(tmp), char): return False
				num = int(tmp)
				tmp = ''
			char = '>'
		else:
			tmp+=str(i)
	if not checkCase(num, int(tmp), char): return False;
	return True
	
Test.assert_equals(correct_signs("3 < 7 < 11"), True)
Test.assert_equals(correct_signs("13 > 44 > 33 > 1"), False)
Test.assert_equals(correct_signs("1 < 2 < 6 < 9 > 3"), True)
Test.assert_equals(correct_signs("4 > 3 > 2 > 1"), True)
Test.assert_equals(correct_signs("5 < 7 > 1"), True)
Test.assert_equals(correct_signs("5 > 7 > 1"), False)
Test.assert_equals(correct_signs("9 < 9"), False)

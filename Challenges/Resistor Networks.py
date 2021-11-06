def convertString(st, s, e, typ):
	arr = []
	tmp = ""
	val = 0.0
	ret = ""
	for i in range(s+1, e):
		if st[i].isdigit():
			tmp += str(st[i])
		elif len(tmp) != 0 and int(tmp) != 0: 
			arr.append(float(tmp))
			tmp = ""
	if len(tmp) != 0 and int(tmp) != 0: 
		arr.append(float(tmp))
	if typ == 'p':
		for i in arr:
			val += i
	elif typ == 's':
		for i in arr:
			val += float(1/i)
		val = float(1/val)
	for i in range(len(st)):
		if i == s:
			ret += str(val)
		elif i > e or i < s:
			ret += str(st[i])
	return ret

def stringToFloat(st):
	ret = ""
	for i in range(len(st)):
		if st[i] == "." and len(st)-i >= 3:
			ret += str(st[i])
			ret += str(st[i+1])
			ret = float(ret)
			if st[i+2] >= st[i+1] or len(st) - i > 4:
				ret += 0.1
			break
		else:
			ret += str(st[i])
	return float(ret)
			

def resist(net):
	lastOpened = ['n',-1]
	allClear = False
	for i in range(len(net)):
		if net[i] == '(':
			lastOpened = ['p',i]
		elif net[i] == ')' and lastOpened[0] == 'p':
			lastOpened[0] = 'n'
			return resist(convertString(net, lastOpened[1], i, 'p'))
		elif net[i] == '[':
			lastOpened = ['s',i]
		elif net[i] == ']' and  lastOpened[0] == 's':
			lastOpened[0] = 'n'
			return resist(convertString(net, lastOpened[1], i, 's'))
		elif lastOpened[0] == 'n' and lastOpened[1] == -1:
			return net
			
class Test:
	def assert_equals(self, ques, ans):
		print(ques)
		
test = Test()

test.assert_equals(resist("(2, 3, 6)"), 11.0)
test.assert_equals(resist("[2, 3, 6]"), 1.0)
test.assert_equals(resist("[10, 20, [30, (40, 50), 60, (70, 80)], 90]"), 4.4)
test.assert_equals(resist("(1, [12, 4, (1, [10, (2, 8)])])"), 3.0)
test.assert_equals(resist("([10, 15], (5, 6, 5))"), 22.0)
test.assert_equals(resist("[22, 6, (10, 18, [33, 15]), (10, [63, 50], 45)]"), 4.0)
test.assert_equals(resist("[([(470, 1000), 330], 470), 680]"), 354.3)
test.assert_equals(resist("([([(470, 680), 330], 1000), 470], 680)"), 1022.0)
test.assert_equals(resist("(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])"), 10.0)

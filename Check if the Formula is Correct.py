from test import Test

def calc(n1,n2,c):
	if c=='+': return int(n1)+int(n2)
	elif c=='-': return int(n1)-int(n2)
	elif c=='*': return int(n1)*int(n2)
	elif c=='/': return int(n1)/int(n2)

def getAns(val):
	print("GET_ANS:",val)
	sym = 'n'
	ind = 0
	num1 = val
	for i in range(len(val)):
		if val[i] == '(':
			cnt = 1
			for j in range(i+1,len(val)):
				if val[j] == '(': cnt+=1
				elif val[j] == ')':
					cnt-=1
					if cnt==0: return getAns(str(val[:i])+str(getAns(val[i+1:j]))+str(val[j+1:]))
		elif not val[i].isdigit() and val[i] != '.':
			if sym == 'n':
				num1 = float(val[ind:i])
				ind = i+1
				sym = val[i]
			else:
				num1 = calc(num1,float(val[ind:i]),sym)
				sym = val[i]
				ind = i+1
	if sym != 'n': num1 = calc(num1,float(val[ind:len(val)]),sym)
	return num1
							
def sepForm(val,index):
	for i in range(index,len(val)):
		if val[i] == '=':
			return getAns(val[index:i]),i+1
		elif i == len(val)-1:
			return getAns(val[index:i+1]),i+1
	return None,0
			
def formula(txt):
	#print("QUES:",txt)
	if len(txt) == 0: return None
	txt = txt.replace(' ','').replace('a','4')
	condition = []
	cIndex = 0
	while True:
		tmp,cIndex = sepForm(txt,cIndex)
		if tmp == None: break
		condition.append(tmp)
	#print('Condition:', condition)
	for i in range(len(condition)):
		if int(condition[0]) != int(condition[i]): return False
	return True
		

Test.assert_equals(formula('6 * 4 = 24'), True)
Test.assert_equals(formula('120 - 7 = 100'), False)
Test.assert_equals(formula('16 - 8 = 16 / 2 = 64 / 8'), True)
Test.assert_equals(formula('a = a'), True)
Test.assert_equals(formula('a * 7 = 90'), False)
Test.assert_equals(formula('16 * 10 = 160 = 14 + 120'), False)
Test.assert_equals(formula('a=4'), True)
Test.assert_equals(formula(''), None)
Test.assert_equals(formula('1000 / 10 = 100 = 2 * 50'), True)
Test.assert_equals(formula('18 / 17 = 2'), False)
Test.assert_equals(formula('(1+2+3+4+5+6+7+8)/a=9'), True)
Test.assert_equals(formula('2 * 2 * 2 = a * 2 = 8'), True)
Test.assert_equals(formula('   8/       9 =       5'), False)
Test.assert_equals(formula('1111           /     101=     11'), True)
Test.assert_equals(formula('a / a = a - 3'), True)

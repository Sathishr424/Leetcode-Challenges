months = "ABCDEHLMPRST"

vov = "aeiou"

def checkIf(x):
	for i in vov:
		if i == x:
			return True
	return False
	
def getSurName(val):
	tmp = ""
	ret = ""
	for i in range(len(val)):
		if not checkIf(val[i].lower()) and len(ret) < 3:
			ret+=str(val[i].upper())
		elif len(ret) >= 3: break
		else: tmp+=str(val[i].upper())
	if (len(ret) < 3):
		for i in tmp:
			if len(ret) < 3:
				ret += str(i)
			else: break
	if (len(ret) < 3):
		for i in range(3-len(ret)):
			ret+="X"
	return ret
	
def getRemaining(dob, gen):
	ret = ""
	ret += dob[-2:]
	dm = []
	tmp = ""
	for i in range(len(dob[:-4])):
		if dob[i] == '/':
			dm.append(int(tmp))
			tmp = ""
		else: tmp+=str(dob[i])
	ret+=months[dm[1]-1]
	
	if gen == 'M':
		if len(str(dm[0])) == 1:
			ret += "0" + str(dm[0])
		else:
			ret += str(dm[0])
	elif gen == 'F':
		ret += str(dm[0] + 40)
		
	return ret
	
def getName(val):
	tmp = ""
	ret = ""
	for i in range(len(val)):
		if not checkIf(val[i].lower()) and len(ret) < 4:
			ret+=str(val[i].upper())
		elif len(ret) >= 4: break
		else: tmp+=str(val[i].upper())
	if (len(ret) < 3):
		for i in tmp:
			if len(ret) < 3:
				ret += str(i)
			else: break
	elif (len(ret) >= 4):
		tmp = ret
		ret = ""
		for i in range(len(tmp)):
			if i != 1:
				ret += tmp[i]
			
	if (len(ret) < 3):
		for i in range(3-len(ret)):
			ret+="X"
	return ret	

def fiscal_code(person):
	ret = ""
	ret += getSurName(person.get('surname'))
	ret += getName(person.get('name'))
	ret +=  getRemaining(person.get('dob'), person.get('gender'))
	return ret
	
class test:
	def assert_equals(self, ques, ans, tmp=""):
		if (ques == ans): print("PASS: " +  str(ques))
		else: print("FAIL " + str(ques) + "|" + str(ans))

Test = test()
	
Test.assert_equals(fiscal_code({ "name": "Brendan", "surname": "Eich", "gender": "M", "dob": "1/12/1961"}), "CHEBND61T01")
Test.assert_equals(fiscal_code({ "name": "Helen", "surname": "Yu", "gender": "F", "dob": "1/12/1950"}), "YUXHLN50T41")
Test.assert_equals(fiscal_code({ "name": "Al", "surname": "Capone", "gender": "M", "dob": "17/1/1899"}), "CPNLAX99A17")
Test.assert_equals(fiscal_code({ "name": "Mickey", "surname": "Mouse", "gender": "M", "dob": "16/1/1928"}), "MSOMKY28A16")
Test.assert_equals(fiscal_code({ "name": "Marie", "surname": "Curie", "gender": "F", "dob": "7/11/1867"}), "CRUMRA67S47")

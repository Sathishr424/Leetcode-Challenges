def reArrange(x,y):
	ret = ""
	spaces = 0
	for i in range(len(x)):
		if x[i] == ' ':
			ret += str(x[i])
			spaces+=1
		else: 
			ret += str(y[i-spaces])
	return ret
	
def adjustIndex(n,l):
	while n>=l:
		n-= l
	return n

def shift_letters(txt, n):
	tmp = txt.replace(' ','')
	ret = list(tmp)
	for i in range(len(tmp)):
		if i+n >= len(tmp):
			ret[adjustIndex((i+n),len(tmp))] = tmp[i]
		else:
			ret[i+n] = tmp[i]
	return reArrange(txt,ret)
	
class test:
	def assert_equals(self, ques, ans, tmp=""):
		if (ques == ans): print("PASS: " +  str(ques))
		else: print("FAIL " + str(ques) + "|" + str(ans))

Test = test()

Test.assert_equals(shift_letters("Made by Harith Shah", 15), "adeb yH arithS hahM")
Test.assert_equals(shift_letters("Boom", 1), "mBoo")
Test.assert_equals(shift_letters("The most addictive way to learn", 19), "add icti vewaytole arn Th emost")
Test.assert_equals(shift_letters("This is a test", 13), "stTh is i sate")
Test.assert_equals(shift_letters("Shift the letters", 1), "sShif tth eletter")
Test.assert_equals(shift_letters("A B C D E F G H", 4), "E F G H A B C D")
Test.assert_equals(shift_letters("Edabit helps you learn in bitesize chunks", 39), "unksEd abith elp syoul ea rninbite sizech")
Test.assert_equals(shift_letters("To be or not to be", 6), "ot to be Tob eo rn")
Test.assert_equals(shift_letters("Made by Harith Shah", 18), "ahMa de byHari thSh")
Test.assert_equals(shift_letters("Boom", 0), "Boom")
Test.assert_equals(shift_letters("The most addictive way to learn", 5), "lea rnTh emostaddi cti ve wayto")
Test.assert_equals(shift_letters("This is a test", 9), "isis at e stTh")
Test.assert_equals(shift_letters("Shift the letters", 3), "ersSh ift thelett")
Test.assert_equals(shift_letters("A B C D E F G H", 10), "G H A B C D E F")
Test.assert_equals(shift_letters("Birds of a Feather Flock Together", 32), "therB ir d sofaFea therF lockToge")
Test.assert_equals(shift_letters("Talk the Talk", 1), "kTal kth eTal")

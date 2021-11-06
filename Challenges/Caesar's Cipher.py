
alp = "abcdefghijklmnopqrstuvwxyz"

def checkAlp(x):
	for i in range(len(alp)):
		if alp[i] == x:
			return i
	return -1
	
def alterIndex(x):
	while x > len(alp)-1:
		x -= len(alp)
	return x
	

def caesar_cipher(s, k):
	ret = ""
	for i in range(len(s)):
		tmp = checkAlp(s[i].lower())
		if tmp == -1:
			ret += str(s[i])
		elif tmp + k >= len(alp):
			if (s[i].isupper()):
				ret += str(alp[alterIndex(tmp+k)]).upper()
			else: ret += str(alp[alterIndex(tmp+k)])
		else:
			if (s[i].isupper()):
				ret += str(alp[tmp+k]).upper()
			else: ret += str(alp[tmp+k])
	return ret

class test:
	def assert_equals(self, ques, ans, tmp=""):
		if (ques == ans): print("PASS: " +  str(ques))

Test = test()

Test.assert_equals(caesar_cipher("middle-Outz", 2), "okffng-Qwvb")
Test.assert_equals(caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 5), "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj")
Test.assert_equals(caesar_cipher("A friend in need is a friend indeed", 20), "U zlcyhx ch hyyx cm u zlcyhx chxyyx")
Test.assert_equals(caesar_cipher("A Fool and His Money Are Soon Parted.", 27), "B Gppm boe Ijt Npofz Bsf Tppo Qbsufe.")
Test.assert_equals(caesar_cipher("One should not worry over things that have already happened and that cannot be changed.", 49), "Lkb pelria klq tloov lsbo qefkdp qexq exsb xiobxav exmmbkba xka qexq zxkklq yb zexkdba.")
Test.assert_equals(caesar_cipher("Back to Square One is a popular saying that means a person has to start over, similar to: back to the drawing board.", 126), "Xwyg pk Omqwna Kja eo w lklqhwn owuejc pdwp iawjo w lanokj dwo pk opwnp kran, oeiehwn pk: xwyg pk pda znwsejc xkwnz.")
			

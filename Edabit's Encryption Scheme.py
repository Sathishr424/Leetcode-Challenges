import math

def encryption(txt):
	ret = ""
	fin = ""
	for i in txt:
		if i != " ":
			fin+=str(i)
	row = int(math.sqrt(len(fin)))
	col = row+1
	if row*col < len(fin):
		row+=1
	for i in range(col):
		for j in range(row):
			if i+(j*col) < len(fin):
				ret += str(fin[i+(j*col)])
		if i < col-1: ret += " "
	return ret
			
class test:
	def assert_equals(self, ques, ans, tmp=""):
		if (ques == ans): print("PASS: " +  str(ques))
		else: print("FAIL " + str(ques) + "|" + str(ans))

Test = test()

Test.assert_equals(encryption("haveaniceday"), "hae and via ecy")
Test.assert_equals(encryption("feedthedog"), "fto ehg ee dd")
Test.assert_equals(encryption("chillout"), "clu hlt io")
Test.assert_equals(encryption("A Fool and His Money Are Soon Parted."), "Anoea FdnSr oHeot oiyoe lsAnd aMrP.")
Test.assert_equals(encryption("One should not worry over things that have already happened and that cannot be changed."), "Onvtlphb. noehreae etraentc swttaech hohhddaa oriayann urnvhnng lygeadoe dosapttd")
Test.assert_equals(encryption("Back to Square One is a popular saying that means a person has to start over, similar to: back to the drawing board."), "Brpgatroea aeutpo,:dr cOlhessbrd knaartiaa. tertsamcw oismoriki Ssaentltn qayahoaog upinavrtb aonssetho")

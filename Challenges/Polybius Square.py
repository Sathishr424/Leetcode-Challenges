
def checkChar(c, grd):
	if c == 'j': c = 'i'
	elif c == ' ': return " "
	for i in range(5):
		for j in range(5):
			if  c == grd[i][j]:
				return (str(i+1) + str(j+1))
	else: return ""
			

def polybius(text):
	alp = "abcdefghiklmnopqrstuvwxyz"
	grid = []
	cnt = 0
	for i in range(5):
		tmp = []
		for j in range(5):
			tmp.append(alp[cnt])
			cnt+=1
		grid.append(tmp)
	ret = ""
	if len(text) >= 1 and text[0].isdigit():
		i=0
		while i < len(text):
			if text[i].isdigit():
				ret += grid[int(text[i])-1][int(text[i+1])-1]
				i+=1
			else:
				ret+=text[i]
			i+=1
	else:
		text = text.lower()
		for i in text:
			ret += checkChar(i,grid)
		
	return ret
	
class Test:
	def assert_equals(self, ques, ans, tmp=""):
		if (ques == ans): print("PASS: " +  ques)
		
test = Test()
	
test.assert_equals(polybius('4323343531242144243322 2443 11 51241344243231154343 1342243215 31242515 3545331323243322 43343215343315 2433 442315 14114225'), "shoplifting is a victimless crime like punching someone in the dark")
test.assert_equals(polybius('Hi'), '2324')
test.assert_equals(polybius("Just because I don't care doesn't mean that I don't understand"), '24454344 12151311454315 24 14343344 13114215 143415433344 32151133 44231144 24 14343344 45331415424344113314', "Disregard punctuation, but keep spaces")
test.assert_equals(polybius('24454344 12151311454315 24 14343344 13114215 143415433344 32151133 44231144 24 14343344 45331415424344113314'), 'iust because i dont care doesnt mean that i dont understand')
test.assert_equals(polybius('543445 14343344 522433 21422415331443 52244423 4311311114'), 'you dont win friends with salad')
test.assert_equals(polybius('The lesson is: never try'), '442315 311543433433 2443 3315511542 444254')

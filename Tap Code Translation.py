from test import Test

def checkCnt(x,c):
	ret = 0
	for i in range(c,len(x)):
		if x[i] == '.':
			ret+=1
		else:
			return ret
	return ret

def getDot(x):
	if x == 'k': x='c'
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == x:
				return (i+1)*'.' + ' ' + (j+1)*'.' + ' '

def tap_code(text):
	ret = ''
	if text[0] == '.':
		cnt = 0
		word = [-1,-1]
		while True:
			if word[0] == -1:
				word[0] = checkCnt(text,cnt)
				cnt += word[0]+1
			elif word[1] == -1:
				word[1] = checkCnt(text,cnt)
				cnt += word[1]+1
			else:
				ret += grid[word[0]-1][word[1]-1]
				word = [-1,-1]
				if cnt >= len(text): break
		return ret
	else:
		for i in text:
			ret+=getDot(i)
		return ret[:-1]

grid = [['a','b','c','d','e'],['f','g','h','i','j'],['l','m','n','o','p'],['q','r','s','t','u'],['v','w','x','y','z']]
	 		

Test.assert_equals(tap_code(".... .... ... .... ... ... .. .... .. .. .. ... .... ...."), "tonight")

Test.assert_equals(tap_code("greeting"), ".. .. .... .. . ..... . ..... .... .... .. .... ... ... .. ..")
Test.assert_equals(tap_code("confrontation"), ". ... ... .... ... ... .. . .... .. ... .... ... ... .... .... . . .... .... .. .... ... .... ... ...")
Test.assert_equals(tap_code("leadership"), "... . . ..... . . . .... . ..... .... .. .... ... .. ... .. .... ... .....")
Test.assert_equals(tap_code("ankle"), ". . ... ... . ... ... . . .....")
#Test.assert_equals(tap_code("extreme"), ". ..... ..... ... .... .... .... .. . ..... ... .. . .....")
Test.assert_equals(tap_code(".... .... ... .... ... ... .. .... .. .. .. ... .... ...."), "tonight")
Test.assert_equals(tap_code("... . ... .... ..... .... . . ... . .... .... ..... ...."), "loyalty")
Test.assert_equals(tap_code(".... .. . ..... .. . . ..... .... .. .... .. . . ... ."), "referral")
Test.assert_equals(tap_code(". ..... ..... ... ... ..... .... .. . ..... .... ... .... ... .. .... ... .... ... ..."), "expression")
Test.assert_equals(tap_code(". . .. . .. . .. .... ... ... .. .... .... .... ..... ...."), "affinity")
Test.assert_equals(tap_code("correspondence"), ". ... ... .... .... .. .... .. . ..... .... ... ... ..... ... .... ... ... . .... . ..... ... ... . ... . .....")
Test.assert_equals(tap_code("atmosphere"), ". . .... .... ... .. ... .... .... ... ... ..... .. ... . ..... .... .. . .....")
Test.assert_equals(tap_code("absolute"), ". . . .. .... ... ... .... ... . .... ..... .... .... . .....")
Test.assert_equals(tap_code("redundancy"), ".... .. . ..... . .... .... ..... ... ... . .... . . ... ... . ... ..... ....")
Test.assert_equals(tap_code("infrastructure"), ".. .... ... ... .. . .... .. . . .... ... .... .... .... .. .... ..... . ... .... .... .... ..... .... .. . .....")
Test.assert_equals(tap_code("... ..... ... .... .. .... ... ... .... ...."), "point")
Test.assert_equals(tap_code("... ..... .... .. . ..... .. . . ..... .... .. . ..... ... ... . ... . ....."), "preference")
Test.assert_equals(tap_code(".. .. .... ..... .. .... . .... . ....."), "guide")
Test.assert_equals(tap_code(". ... .. ... . . .... .. . . . ... .... .... . ..... .... .. .. .... .... ... .... .... .. .... . ..."), "characteristic")
Test.assert_equals(tap_code(". ... ... .... ... .. ... .. . ..... .... .. . ... . ....."), "commerce")

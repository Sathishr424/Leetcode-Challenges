
def tmp(x,y):
	ret = [i for i in range(len(y))]
	for i in range(len(x)):
		for j in range(len(y)):
			if x[i] == y[j]:
				ret[j] = i
	return ret

alp = [i for i in "abcdefghijklmnopqrstuvwxyz"]
vov = "aeiou"
vovNum = tmp(alp, vov)
print(vovNum)

def checkIf(x):
	for i in vov:
		if x == i:
			return 0
	m = vovNum[0]
	diff = m-x
	for j in vovNum:
		if j-:
			

def distanceToNearestVowel(st):
	ret = []
	for i in range(len(st)):
		if 
	
#print(distanceToNearest())

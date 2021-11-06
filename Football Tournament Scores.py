from test import Test

#This code not only work with one length of integer also work with any length of integers.
#There is no need to have only four teams you can have how many teams u want
#And Team name also not to be one character

def decodeScore(st):
	ret = ['t1', 't1s', 't2', 't2s']
	tmp = ""
	for i in st:
		if i != ' ':
			tmp+=str(i)
		else:
			if tmp != '-':
				if ret[0] == 't1':
					ret[0] = tmp
				elif ret[1] == 't1s':
					ret[1] = tmp
				elif ret[3] == 't2s':
					ret[3] = tmp
			tmp = ""
	ret[2] = tmp
	return ret			
		
def checkArr(arr, x):
	for i in range(len(arr)):
		if arr[i].name == x: 
			return i
	return -1
	
class teamManagement:
	def __init__(self, name, points, goals, concededGoals):
		self.name = name
		self.points = points
		self.goals = goals
		self.concededGoals = concededGoals
	
	def getInfo(self):
		return [self.name, self.points, self.goals, self.goals-self.concededGoals]
		
def bubbleSort(arr):
	done = True
	for i in range(len(arr)-1):
		if arr[i].points > arr[i+1].points:
			done = False
			arr[i], arr[i+1] = arr[i+1], arr[i]
		elif arr[i].points == arr[i+1].points:
			if arr[i].goals > arr[i+1].goals:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				done = False
			elif arr[i].goals == arr[i+1].goals and arr[i].concededGoals < arr[i+1].concededGoals:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				done = False
	if done:
		return arr[::-1]
	return bubbleSort(arr)
	
def tournament_scores(lst):
	teams = []
	for i in lst:
		decoded = decodeScore(i)
		t1 = checkArr(teams, decoded[0])
		t2 = checkArr(teams, decoded[2])
		if t1 == -1:
			teams.append(teamManagement(decoded[0],0,0,0))
			t1 = len(teams)-1
		if t2 == -1:
			teams.append(teamManagement(decoded[2],0,0,0))
			t2 = len(teams)-1
		teams[t1].goals+=int(decoded[1])
		teams[t2].goals+=int(decoded[3])
		teams[t1].concededGoals+=int(decoded[3])
		teams[t2].concededGoals+=int(decoded[1])
		if decoded[1] > decoded[3]:
			teams[t1].points+=3
		elif decoded[3] > decoded[1]:
			teams[t2].points+=3
		else: 
			teams[t1].points+=1
			teams[t2].points+=1
	order = []
	teams = bubbleSort(teams)
	return [i.getInfo() for i in teams]
				
	
print(tournament_scores(["XY 52 - 25 WX", "AB 0 - 201 BC", "CD 2 - 502 DE", "BC 0 - 25 CD", "DE 0 - 32 AB", "AB 0 - 2 CD", "BC 3 - 1 DE"]))
print("\n\n")
Test.assert_equals(tournament_scores(["A 0 - 1 B", "C 2 - 0 D", "B 2 - 2 C", "D 3 - 1 A", "A 2 - 2 C", "B 2 - 0 D"]), [["B", 7, 5, 3], ["C", 5, 6, 2], ["D", 3, 3, -2], ["A", 1, 3, -3]], "Example #1");
Test.assert_equals(tournament_scores(["A 0 - 0 B", "C 3 - 5 D", "B 1 - 0 C", "D 1 - 1 A", "A 2 - 2 C", "B 1 - 0 D"]), [["B", 7, 2, 2], ["D", 4, 6, 1], ["A", 3, 3, 0], ["C", 1, 5, -3]]);
Test.assert_equals(tournament_scores(["A 4 - 0 B", "C 2 - 1 D", "B 1 - 0 C", "D 3 - 2 A", "A 1 - 3 C", "B 2 - 1 D"]), [["C", 6, 5, 2], ["B", 6, 3, -2], ["A", 3, 7, 1], ["D", 3, 5, -1]], "Example #2");
Test.assert_equals(tournament_scores(["A 3 - 3 B", "C 0 - 6 D", "B 4 - 2 C", "D 0 - 1 A", "A 1 - 2 C", "B 2 - 1 D"]), [["B", 7, 9, 3], ["A", 4, 5, 0], ["D", 3, 7, 4], ["C", 3, 4, -7]]);
Test.assert_equals(tournament_scores(["A 2 - 1 B", "C 3 - 0 D", "B 1 - 1 C", "D 1 - 0 A", "A 3 - 0 C", "B 2 - 4 D"]), [["A", 6, 5, 3], ["D", 6, 5, 0], ["C", 4, 4, 0], ["B", 1, 4, -3]], "Example #3");
Test.assert_equals(tournament_scores(["A 0 - 1 B", "C 2 - 0 D", "B 0 - 0 C", "D 0 - 1 A", "A 0 - 2 C", "B 3 - 1 D"]), [["C", 7, 4, 4], ["B", 7, 4, 3], ["A", 3, 1, -2], ["D", 0, 1, -5]]);
Test.assert_equals(tournament_scores(["AB 0 - 1 BC", "CD 2 - 0 DE", "BC 0 - 0 CD", "DE 0 - 1 AB", "AB 0 - 2 CD", "BC 3 - 1 DE"]), [["CD", 7, 4, 4], ["BC", 7, 4, 3], ["AB", 3, 1, -2], ["DE", 0, 1, -5]]);
	

from test import Test

def subFun(lst, k, rem):
	while True:
		tmp = []
		for i in range(len(lst)):
			if rem+1 == k:
				rem = 0
			else:
				tmp.append(lst[i])
				rem+=1
		lst = tmp
		if len(lst) == 2 and 1+rem==k: return lst[1]
		elif len(lst) == 2 and 2+rem==k: return lst[0]

def who_goes_free(n, k):
	lst = []
	rem = 0
	for i in range(n):
		if (i+1)%k != 0: 
			lst.append(i)
			rem+=1
		else: rem = 0
	return subFun(lst, k,rem)
	
Test.assert_equals(who_goes_free(9, 2), 2)
Test.assert_equals(who_goes_free(9, 3), 0)
Test.assert_equals(who_goes_free(7, 2), 6)
Test.assert_equals(who_goes_free(7, 3), 3)
Test.assert_equals(who_goes_free(15, 4), 12)
Test.assert_equals(who_goes_free(14, 3), 1)
Test.assert_equals(who_goes_free(53, 7), 21)
Test.assert_equals(who_goes_free(543, 21), 455)
Test.assert_equals(who_goes_free(673, 13), 303)
		

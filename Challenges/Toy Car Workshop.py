def cars(wheels, bodies, figures):
	cnt = 0
	for i in range(bodies):
		if wheels >= 4 and figures >= 2:
			cnt+=1
			wheels-=4; figures-=2;
	return cnt

class test:
	def assert_equals(self, ques, ans, tmp=""):
		if (ques == ans): print("PASS: " +  str(ques))

Test = test()

Test.assert_equals(cars(37, 15, 20), 9)
Test.assert_equals(cars(72, 7, 21), 7)
Test.assert_equals(cars(9, 44, 34), 2)
Test.assert_equals(cars(50, 38, 7), 3)
Test.assert_equals(cars(68, 9, 44), 9)
Test.assert_equals(cars(3, 29, 54), 0)
Test.assert_equals(cars(28, 34, 80), 7)
Test.assert_equals(cars(88, 50, 83), 22)
Test.assert_equals(cars(66, 18, 21), 10)
Test.assert_equals(cars(97, 6, 10), 5)
Test.assert_equals(cars(921, 310, 350), 175)
Test.assert_equals(cars(736, 430, 851), 184)
Test.assert_equals(cars(405, 379, 740), 101)
Test.assert_equals(cars(593, 78, 389), 78)
Test.assert_equals(cars(875, 370, 675), 218)
Test.assert_equals(cars(863, 274, 203), 101)
Test.assert_equals(cars(959, 331, 537), 239)
Test.assert_equals(cars(416, 340, 551), 104)
Test.assert_equals(cars(692, 348, 543), 173)
Test.assert_equals(cars(527, 412, 951), 131)

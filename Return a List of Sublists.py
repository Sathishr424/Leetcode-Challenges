from test import Test

def matrix(x, y, z):
	ret = []
	for i in range(x):
		tmp = []
		for j in range(y):
			tmp.append(z)
		ret.append(tmp)
	return ret

Test.assert_equals(matrix(3, 4, 0), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
Test.assert_equals(matrix(2, 3, "#"), [["#", "#", "#"], ["#", "#", "#"]])
Test.assert_equals(matrix(2, 3, -4), [[-4, -4, -4], [-4, -4, -4]])
Test.assert_equals(matrix(1, 2, 0), [[0, 0]])

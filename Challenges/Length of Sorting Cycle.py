from test import Test

def cycle_length(lst, n):
    lstSorted = sorted(lst)
    if lst[lst.index(n)] == lstSorted[lst.index(n)]: return 0
    index = 0
    ret = 0
    for i in range(len(lst)):
        if lst[i] == n: index = i
    while True:
        for i in range(len(lstSorted)):
            if lstSorted[i] == lst[index]:
                lst[index], lst[i] = lst[i], lst[index]
                if lst[index] == lstSorted[index] and lst[i] == lstSorted[i]: return ret+1
                elif lst[index] == lstSorted[index]: return ret+1
                ret += 1
                break
            
Test.assert_equals(cycle_length([1, 5, 4, 3, 2, 6], 4), 1)
Test.assert_equals(cycle_length([1, 5, 4, 3, 2, 6], 6), 0)
Test.assert_equals(cycle_length([1, 5, 4, 3, 2, 6], 5), 1)
Test.assert_equals(cycle_length([1, 4, 2, 3, 5], 4), 2)
Test.assert_equals(cycle_length([11, 44, 22, 31, 50], 44), 2)
Test.assert_equals(cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 7), 7)
Test.assert_equals(cycle_length([43, 81, 88, 93, 17, 32, 19, 11], 93), 5)
Test.assert_equals(cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 1), 0)
Test.assert_equals(cycle_length([1, 6, 7, 2, 4, 3, 9, 8, 5], 6), 6)
Test.assert_equals(cycle_length([1, 6, 7, 2, 4, 3, 9, 8, 5], 5), 6)
Test.assert_equals(cycle_length([1, 6, 7, 2, 4, 3, 9, 8, 5], 2), 6)
Test.assert_equals(cycle_length([1, 6, 7, 2, 4, 3, 9, 8, 5], 3), 6)
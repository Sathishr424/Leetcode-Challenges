from test import Test

def bubbleSort(lst):
    sort = True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i]
            if sort: sort=False
    if not sort:
        bubbleSort(lst)

def removeDuplicates(lst):
    ret = [lst[0]]
    for i in range(1,len(lst)):
        if lst[i] != ret[-1]:
            ret.append(lst[i])
    return ret
        
def unique_sort(lst):
    bubbleSort(lst)
    return removeDuplicates(lst)
        
# Test.assert_equals(
#   unique_sort([1, 5, 8, 2, 3, 4, 4, 4, 10]),
#   [1, 2, 3, 4, 5, 8, 10]
# )

# Test.assert_equals(
#     unique_sort([1, 2, 5, 4, 7, 7, 7]),
#   [1, 2, 4, 5, 7]
# )
# 
Test.assert_equals(
    unique_sort([7, 6, 5, 4, 3, 2, 1, 0, 1]),
  [0, 1, 2, 3, 4, 5, 6, 7]
)
# 
# Test.assert_equals(
#     unique_sort([3, 6, 5, 4, 3, 27, 1, 100, 1]),
#   [1, 3, 4, 5, 6, 27, 100]
# )
# 
# Test.assert_equals(
#     unique_sort([-9, -3.1414, -87, 8, -4.323827, -3.1415, -3.1415]),
#   [-87, -9, -4.323827, -3.1415, -3.1414, 8]
# )
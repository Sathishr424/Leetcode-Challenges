# Definition for singly-linked list.

def listNodeToNum(node):
    arr = []
    while node != None:
        arr.append(str(node.val))
        node = node.next
    return ''.join(arr)

def arrToListNode(arr,ind):
    if ind < len(arr): return ListNode(arr[ind],arrToListNode(arr,ind+1))
    return None

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        return arrToListNode(list(str(int(listNodeToNum(l1)) + int(listNodeToNum(l2)))),0)

print(listNodeToNum(Solution().addTwoNumbers(arrToListNode([7,2,4,3],0),arrToListNode([5,6,4],0))))
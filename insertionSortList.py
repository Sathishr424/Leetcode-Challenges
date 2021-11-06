
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        prevNode = head
        currNode = head.next
        nextNode = currNode.next
        while currNode != None:
            if currNode.val > nextNode.val:
                while currNode.val
                
 
def arrToListNode(arr,ind):
    if ind < len(arr): return ListNode(arr[ind],arrToListNode(arr,ind+1))
    return None
       
print(Solution().insertionSortList(arrToListNode([4,2,1,3],0)))
# x = arrToListNode([4,2,1,3],0)
# print(x.val)
# 
# while x.next != None:
#     x = x.next
#     print(x.val)
        
def decToBin(num,val=""):
    print(num%2,end='')
    if num > 1: return val+decToBin(num // 2,str(num%2))
    return val

def binToDec(binary):
    print(binary)
    ret = 0;
    for i in range(len(binary)):
        ret += int(binary[i]) * (2**((len(binary)-1)-i))
    return ret

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def getDecimalValue(self, head):
        node = head
        length = 0
        ret = 0
        while node != None:
            length += 1
            node = node.next
        node = head
        cnt = 0
        while node != None:
            cnt += 1
            ret += int(node.val) * (2**(length-cnt))
            node = node.next
        return ret
    
def arrToListNode(arr,ind):
    if ind < len(arr): return ListNode(arr[ind],arrToListNode(arr,ind+1))
    return None

print(str(binToDec("10010")))
print(Solution().getDecimalValue(arrToListNode(list("10010"),0)))
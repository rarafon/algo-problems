# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        forward1 = head
        forward2 = head

        cyclenode = None

        while True:
            forward2 = forward2.next
            if forward2 == None:
                return None
            forward2 = forward2.next
            if forward2 == None:
                return None
            
            forward1 = forward1.next
            if forward1 == forward2:
                cyclenode = forward1
                break

        start = end = cyclenode
                
        cyclesize = 1
        cyclenode = cyclenode.next

        while cyclenode != start:
            cyclesize += 1
            end = cyclenode
            cyclenode = cyclenode.next
        
        while start != end:
            cyclenode = start.next
            cyclesize = 2
            while cyclenode != end:
                cyclesize += 1
                cyclenode = cyclenode.next
            
            if cyclesize == 1:
                return start
            count = int(cyclesize/2)
            # print(start.val, end.val, "sized", cyclesize)

            cyclenode = start
            while count > 0:
                cyclenode = cyclenode.next
                count -= 1
            mid = cyclenode
            # print("m", start.val, mid.val, end.val)

            cyclenode = head
            while cyclenode != start and cyclenode != end and cyclenode != mid:
                cyclenode = cyclenode.next
            
            if cyclesize == 2 and cyclenode == end:
                # print("a")
                return end
            
            if cyclenode == start:
                # print("b")
                return start
            elif cyclenode == mid:
                # print("c")
                end = mid
            else:
                # print("d")
                start = mid
        return start

def create_cycle(values, loop_index):
    start = ListNode(values[0])
    if len(values) == 1:
        return start
    prev = start

    looped = None
    if loop_index == 0:
        looped = start

    for i in range(1, len(values)):
        n = ListNode(values[i])
        if loop_index == i:
            looped = n
        prev.next = n
        prev = n
    end = n
    if loop_index >= 0:
        end.next = looped
    return start
    
s = Solution()

print(s.detectCycle(create_cycle([3,2,0,-4],1)).val, 2)
print(s.detectCycle(create_cycle([3,2,0,-4],-1)), None)
print(s.detectCycle(create_cycle([3],-1)), None)
print(s.detectCycle(create_cycle([3,2,0,-4],2)).val, 0)
print(s.detectCycle(create_cycle([3,2,0,-4],3)).val, -4)
print(s.detectCycle(create_cycle([3,2,1,22,3,4,5,6,7,3,10,4,3,50,-4],3)).val, 22)
print(s.detectCycle(create_cycle([3,2,1,22,3,4,5,6,7,3,10,4,3,50,-4],0)).val, 3)
print(s.detectCycle(create_cycle([3,2,1,22,3,4,5,6,7,3,10,4,3,50,-4],0)).val, 3)
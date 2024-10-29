# 23. Merge k Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Add a counter to handle duplicate values
        heap = []
        counter = 0
        
        # Push initial nodes with a counter to break ties
        for list_ in lists:
            if list_:
                heapq.heappush(heap,(list_.val,counter,list_))
                counter += 1

        dummy = ListNode(-1)
        curr = dummy

        while len(heap):
            currMin,counter,node = heapq.heappop(heap)
            curr.next = node
            
            
            if node.next:
                heapq.heappush(heap,(node.next.val,counter,node.next))
                counter += 1

            curr = curr.next

        return dummy.next

# In Python, when two tuples have the same first element (in this case, the same val), the heap will try to compare the second elements to break the tie. In this case, the second element is a ListNode, which doesn't have a defined comparison method. This will raise a TypeError when two nodes have the same value.
# Add a counter variable to create unique tuples even when values are the same



        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        currentNode = head
        nextSet = set()

        while currentNode.next:
            if currentNode.next in nextSet:
                return True
            nextSet.add(currentNode)
            currentNode = currentNode.next

        return False
        

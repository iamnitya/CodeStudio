# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        front = head
        rear = head
        while rear!=None and rear.next!=None:
            front = front.next
            rear = rear.next.next
            if rear==front:
                return True
        return False


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: Optional[ListNode]
#         :type l2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
        
# def addTwoNumbers(l1, l2):
#     """
#     :type l1: Optional[ListNode]
#     :type l2: Optional[ListNode]
#     :rtype: Optional[ListNode]
#     """
#     current1 = None
#     current2 = None
#     head1 = l1
#     head2 = l2
#     current1 = head1
#     current2 = head2
#     currentAdd1 = ""
#     currentAdd2 = ""
#     while current1 or current2:
#         if current1:
#             currentAdd1 += str(current1.val)
#             current1 = current1.next
#         if current2:
#             currentAdd2 += str(current2.val)
#             current2 = current2.next
        
#     total = int(str(int(currentAdd1[::-1]) + int(currentAdd2[::-1]))[::-1])
    
#     head = None
#     current = None
#     for i in range(len(str(total))):
#         node = ListNode(int(str(total)[i]))
#         if head is None:
#             head = node
#             current = node
#         else:
#             current.next = node
#             current = node
#     return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next   
        
def addTwoNumbers(l1,l2):
    head = None
    current = None
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total_sum = val1 + val2 + carry
        
        digit = total_sum % 10
        carry = total_sum // 10
        
        if l1: l1 = l1.next
        if l2: l2 = l2.next
            
        node = ListNode(digit)
        if head is None:
            head = node
            current = node
        else:
            current.next = node
            current = node
        print(digit)
    return head
# Testing
l1 = [2, 4, 3]
l2 = [5, 6, 4]


def createLinkedList(values):
    head = None
    current = None

    for value in values:
        node = ListNode(value)

        if head is None:
            head = node
            current = node
        else:
            current.next = node
            current = node

    return head


l1 = createLinkedList(l1)
l2 = createLinkedList(l2)

addTwoNumbers(l1, l2)

# Notes 
# convert list into one whole int, add both lists that are converted,
# total result convert back to string use reverse
# help(list) works
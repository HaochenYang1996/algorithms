# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=None
        tail=None
        carry=0

        while True and (l1 or l2):
            # current number in l1
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0;


            # current number in l2
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0;


            # total of these two numbers 
            number = num1+num2+carry


            # when the sum of these two number >10, carry is 1, minus this number by 10     
            if number>=10:
                carry = 1
                number -= 10
            else:
                carry = 0


            # linked list operation
            if not tail:
                # if tail is empty, change tail and head
                tail = ListNode(number)
                head = tail
            else:
                # every time we have a new number, push it into the back of the list
                tail.next = ListNode(number)
                tail = tail.next

        # if we still have a final carry, add it to the back
        if carry == 1:
            tail.next = ListNode(1)

        return head 


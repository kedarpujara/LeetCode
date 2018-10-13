# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        curr = 0
        dummy = ListNode(-1)
        while l1 and l2:
            curr = l1.val + l2.val + carry
            if curr > 10:
                carry = 1
                curr = curr-10
            dummy.next = ListNode(curr)
            
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            dummy.next = l1
        
        if l2:
            dummy.next = l2

        return dummy.next














    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     carry = 0
    #     curr = 0
    #     first_num = True
    #     new = ListNode(-1)
    #     print new.val
    #     #ret_list
    #     #ret_list = ListNode(l1.val + l2.val)        
    #     while l1 != None and l2 != None:
    #         if l1 != None and l2 != None:
    #             curr = l1.val + l2.val + carry
    #             if first_num:
    #                 ret_list = ListNode(curr)
    #                 first_num = False
    #             else:
    #                 if curr > 9:
    #                     carry = 1
    #                     curr = curr - 10
    #                 else:
    #                     carry = 0
                                       
    #             l1 = l1.next
    #             l2 = l2.next
    #             ret_list.next = ListNode(curr) 
    #             print curr
                
    #         elif l1 != None:
    #             curr = l1.val + carry
    #             if first_num:
    #                 ret_list = ListNode(curr)
    #                 first_num = False
    #             else:
    #                 if curr > 9:
    #                     carry = 1
    #                     curr = curr-10
    #                 else:
    #                     carry = 0
    #             ret_list.next = ListNode(curr)
    #             l1.next
    #         elif l2 != None:
    #             curr = l2.val + carry
    #             if first_num:
    #                 ret_list = ListNode(l2.val)
    #                 first_num = False
    #             else:
    #                 curr = l2.val + carry
    #                 if curr > 9:
    #                     carry = 1
    #                     curr = curr-10
    #                 else:
    #                     carry = 0
    #                 l2 = l2.next
    #                 ret_list.next = ListNode(curr)
    #         print curr
    #     return ret_list
                
    #             
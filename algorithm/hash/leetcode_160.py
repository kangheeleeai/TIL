# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        case_1 = headA
        case_2 = headB
        
        saving_dict={}
        while case_1 is not None:
            saving_dict[case_1]=True
            case_1 = case_1.next
            
        while case_2 is not None:
            if saving_dict.get(case_2):
                return case_2
            case_2 = case_2.next
            
        return None
		

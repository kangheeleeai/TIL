#https://leetcode.com/problems/middle-of-the-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s_no, m_no=head,head
        end_num = 1
        while s_no.next:
            s_no = s_no.next
            end_num += 1
        m_num=end_num//2
        while True:
            if m_num==0:
                return m_no
            m_no = m_no.next
            m_num -= 1 

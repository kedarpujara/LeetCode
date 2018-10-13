/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode l3;
        if(l1.val >= l2.val){
            l3 = new ListNode(l1.val);
            l1 = l1.next;
        } else {
            l3 = new ListNode(l2.val);
            l2 = l2.next;
        }

        while(l1.next != null && l2.next != null){
            if(l1.val <= l2.val){
                l3.next.val = l1.val;
                l1 = l1.next;
            } else {
                l3.next.val = l2.val;
                l2 = l2.next;
            }
        }
        return l3;
    }
}

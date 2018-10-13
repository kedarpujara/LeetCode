/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class Solution {
    public ListNode swapPairs(ListNode head) {
    	
    	ListNode curr = new ListNode(-1);
    	ListNode dummy = curr;
    	while(head != null && head.next != null){
    		curr.next = head.next;
    		curr.next.next = head;
    		curr = curr.next.next;
    		head = head.next.next;
    	}
    	return dummy.next;
    }
}
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        
        if (head == null) return null;
        
        ListNode curr = head;
        ListNode mobile = head.next;
        
        while(mobile != null){
            if (mobile.val == curr.val){
                mobile = mobile.next;
                curr.next = null;
            }
            else{
                curr.next = mobile;
                curr = curr.next;
                mobile = mobile.next;
            }
        }
        
        return head;
    }
}
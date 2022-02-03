/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null) return null;
        
        HashSet<ListNode> h = toHashSet(headA);
        
        return checkOcurrences(headB, h);
    }

    private ListNode checkOcurrences(ListNode node, HashSet<ListNode> hashNode){
        while(node != null){
            if (hashNode.contains(node)){
                return node;
            }
            node = node.next;
        }
        return null;
    }
    
    private HashSet<ListNode> toHashSet(ListNode node){
        HashSet<ListNode> h = new HashSet<>();
        
        while(node != null){
            h.add(node);
            node = node.next;
        }
        
        return h;
    }
}
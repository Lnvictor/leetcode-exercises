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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        boolean isIncreased = false;

        Integer[] arrayL1 = elementsOfNode(l1);
        Integer[] arrayL2 = elementsOfNode(l2);
        int max = Math.max(arrayL1.length, arrayL2.length);
        ListNode resp = new ListNode(0);
        ListNode temp = resp;

        for (int i = 0; i < max; i++){
            int tempVal;
            if(i < arrayL1.length && i < arrayL2.length){
                tempVal = arrayL1[i] + arrayL2[i];
            }

            else if(i >= arrayL1.length){
                tempVal = arrayL2[i];
            }
            else{
                tempVal = arrayL1[i];
            }
            
            if (tempVal + temp.val >= 10){
                temp.val = (temp.val + tempVal) % 10;
                isIncreased = true;
            }
            else  temp.val += tempVal;

            if (i < max - 1) {
                if (isIncreased) {
                    temp.next = new ListNode(1);
                    isIncreased = false;
                } else temp.next = new ListNode(0);
                temp = temp.next;
            }
        }

        if (isIncreased){
            temp.next = new ListNode(1);
        }
        return resp;
    }
    
    private Integer[] elementsOfNode(ListNode node){
        int current = node.val;
        int currentPosition = 0;
        List<Integer> resp = new ArrayList<>();
        ListNode next = node.next;

        while(next != null){
            resp.add(current);
            current = next.val;
            next = next.next;
        }

        if(resp.size() == 0){
            resp.add(node.val);
        }
        else{
            resp.add(current);
        }

        return resp.toArray(new Integer[resp.size()]);
    }
}
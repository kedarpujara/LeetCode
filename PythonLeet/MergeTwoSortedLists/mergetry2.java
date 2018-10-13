class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        boolean isFirst = true;
        if(l2 == null){
            return l1;
        }
        if(l1 == null){
            return l2;
        }
        ListNode new_list = new ListNode(-1);
        while(l1 != null || l2 != null){
            if(l1 != null && l2 != null){
                if(l1.val <= l2.val){
                    if(isFirst){
                        //ListNode new_list = new ListNode(l1.val);
                        new_list = l1;
                        isFirst = false;
                        l1 = l1.next;
                    } else {
                        new_list.next = l1;
                        l1 = l1.next;
                    }

                }
                else{
                    if(isFirst){
                        //ListNode new_list = new ListNode(l2.val);
                        new_list= l2;
                        isFirst = false;
                        l2 = l2.next;
                    } else {
                        new_list.next = l2;
                        l2 = l2.next;
                    }

                }
            }
            new_list = new_list.next;
        }

        while(l1 != null){
            new_list.next = l1;
            l1 = l1.next;
            new_list = new_list.next;
        }
        while(l2 != null){
            new_list.next = l2;
            l2 = l2.next;
            new_list = new_list.next;
        }
        return new_list;
    }
}

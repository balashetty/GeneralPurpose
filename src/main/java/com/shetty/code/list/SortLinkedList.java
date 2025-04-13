package com.shetty.code.list;

public class SortLinkedList {

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(0);
        head.next.next = new ListNode(2);
        head.next.next.next = new ListNode(1);
        head.next.next.next.next = new ListNode(2);

        System.out.println("Linked list before sorting:");
        printList(head);

        head = sortList(head);

        System.out.println("Linked list after sorting:");
        printList(head);
    }

    public static ListNode sortList(ListNode head) {
    	int[] counts = {0, 0, 0};
    	
    	ListNode cur= head;
    	
    	while (cur != null) {
    		counts[cur.data]++;
    		cur = cur.next;
    	}
    	
    	int i =0;
    	cur= head;
    	
    	while(cur != null) {
    		if (counts[i] == 0 ) {
    			i++;
    		} else {
    			cur.data = i;
    			counts[i]--;
    			cur = cur.next;
    		}
    	}
    	
    	return head;
    }
    
	public static ListNode sortList0(ListNode head) {
		int[] count = {0,0,0};
		ListNode current = head;
		
		while (current != null) {
			count[current.data]++;
			current = current.next;
		}
		
		current = head;
		
		int i = 0;
		
		while (current != null) {
			if (count[i] == 0) {
				i++;
			} else {
				current.data = i;
				count[i]--;
				current = current.next;
			}
		}
		
		return head;
	}

    public static ListNode sortList1(ListNode head) {
        int[] count = {0, 0, 0};
        ListNode current = head;

        while (current != null) {
            count[current.data]++;
            current = current.next;
        }

        current = head;
        int i = 0;

        while (current != null) {
            if (count[i] == 0) {
                i++;
            } else {
                current.data = i;
                count[i]--;
                current = current.next;
            }
        }

        return head;
    }

    public static void printList(ListNode head) {
        ListNode temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
}

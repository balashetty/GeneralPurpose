package com.shetty.code.doublelist;

public class DoublyLinkedList {
    ListNode head;

    // Partitions the list around a pivot
    ListNode partition(ListNode low, ListNode high) {
        int pivot = high.data;
        ListNode i = low.prev;

        for (ListNode j = low; j != high; j = j.next) {
            if (j.data <= pivot) {
                i = (i == null) ? low : i.next;
                swap(i, j);
            }
        }
        i = (i == null) ? low : i.next;
        swap(i, high);
        return i;
    }

    // Recursive function to perform Quicksort
    void quickSort(ListNode low, ListNode high) {
        if (high != null && low != high && low != high.next) {
            ListNode pivot = partition(low, high);
            quickSort(low, pivot.prev);
            quickSort(pivot.next, high);
        }
    }

    // Helper function to swap data of two nodes
    void swap(ListNode node1, ListNode node2) {
        int temp = node1.data;
        node1.data = node2.data;
        node2.data = temp;
    }

     // Helper function to get the last node
    ListNode getLastNode(ListNode listNode) {
        while (listNode != null && listNode.next != null) {
            listNode = listNode.next;
        }
        return listNode;
    }

    // Method to add a node at the end of the list
    void append(int data) {
        ListNode newNode = new ListNode(data);
        if (head == null) {
            head = newNode;
            return;
        }
        ListNode last = getLastNode(head);
        last.next = newNode;
        newNode.prev = last;
    }

    // Method to print the linked list
    void printList() {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        DoublyLinkedList list = new DoublyLinkedList();
        list.append(5);
        list.append(2);
        list.append(8);
        list.append(1);
        list.append(9);

        System.out.println("Linked List before sorting:");
        list.printList();

        ListNode lastNode = list.getLastNode(list.head);
        list.quickSort(list.head, lastNode);

        System.out.println("Linked List after sorting:");
        list.printList();
    }
}
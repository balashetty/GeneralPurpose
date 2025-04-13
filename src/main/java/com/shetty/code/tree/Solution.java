package com.shetty.code.tree;

import java.util.HashMap;
import java.util.Map;

public class Solution {

	public static void main(String[] args) {
//		 BinaryTree tree = new BinaryTree();
//
//	        tree.root = new Node(1);
//	        tree.root.left = new Node(2);
//	        tree.root.right = new Node(3);
//	        tree.root.left.left = new Node(4);
//	        tree.root.left.right = new Node(5);
//
//	        System.out.println("The height of binary tree is: " +
//	                tree.findHieght(tree.root));
	        
//	        ListNode n1 = new ListNode(1);
//			ListNode n2 = new ListNode(2);
//			ListNode n3 = new ListNode(3);
//			ListNode n4 = new ListNode(4);
//			ListNode n5 = new ListNode(5);
//			n1.next = n2;
//			n2.next = n3;
//			n3.next = n4;
//			n4.next = n5;
//			ListNode head = n1;
//	        showLinkedList(head);
//	        head = reverseLinkedList(head);
//	        showLinkedList(head);
		 TreeNode n0 = new TreeNode(5);

		 TreeNode n1 = new TreeNode(4);
		 TreeNode n2 = new TreeNode(11);
		 TreeNode n3 = new TreeNode(7);
		 TreeNode n4 = new TreeNode(7);
		 TreeNode n5 = new TreeNode(10);
		 TreeNode n6 = new TreeNode(21);
		 n0.left = n1;
		 n1.left = n2;
		 n2.left = n3;
		 n2.right = n4;
		 n1.right = n5;
		 n1.right = n6;
		 int sum = n1.val + n2.val + n3.val ;
		 System.out.println("has sum :" + sum + " ," + hasPathSum(n0, 22));
		 
	}

	static class BinaryTree {
		TreeNode root;
		public int findHieght(TreeNode listNode) {
			if (listNode == null) {
				return 0;
			}
			
			int leftHight = findHieght(listNode.left);
			int rightHeight = findHieght(listNode.right);
			
			return Math.max(leftHight, rightHeight) + 1;
		}
	}
	
	static int target;
    
    public static boolean hasPathSum(TreeNode root, int targetSum) {
        target = targetSum;
        return dfs(root, 0);
    }
    
    public static boolean dfs(TreeNode node, int curr) {
        if (node == null) {
            return false;
        }
        
        if (node.left == null && node.right == null) {
            return (curr + node.val) == target;
        }
        
        curr += node.val;
        boolean left = dfs(node.left, curr);
        boolean right = dfs(node.right, curr);
        return left || right;
    }

}

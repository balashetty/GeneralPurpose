package com.shetty.code.tree;

public class TreeNode {
	public int val;
	public TreeNode left;
	public TreeNode right;

	TreeNode(int val) {
		this.val = val;
	}

	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
	
	public static TreeNode of(Integer [] arr) {
		return buildTree(arr, 0);
	}
	
	static TreeNode buildTree(Integer[] arr, int index) {
        if (index < 0 || index >= arr.length || arr[index] == null || arr[index] == -1) {
            return null;
        }

        TreeNode root = new TreeNode(arr[index]);
        root.left = buildTree(arr, 2 * index + 1);
        root.right = buildTree(arr, 2 * index + 2);

        return root;
    }
}

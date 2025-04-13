package com.shetty.code.practice;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

import com.shetty.code.tree.TreeNode;

public class KthSmallestElement {

	public static void main(String[] args) {
		KthSmallestElement solution = new KthSmallestElement();
		
		Integer [] arr = {5,3,6,2,4,null,null,1};
		TreeNode root = TreeNode.of(arr);
		int thirdEl = solution.kthSmallest(root, 3);
		System.out.println("3rd element in the array :" + Arrays.toString(arr) + ", is :" + thirdEl);
		
		int secondEl = solution.kthSmallest(root, 2);
		System.out.println("3rd element in the array :" + Arrays.toString(arr) + ", is :" + secondEl);
		
		int sexthEl = solution.kthSmallest(root, 6);
		System.out.println("3rd element in the array :" + Arrays.toString(arr) + ", is :" + sexthEl);
	}

	public int kthSmallest(TreeNode root, int k) {
		List<Integer> inorderNodes = new LinkedList<>();
		dfsInorder(root, inorderNodes);
		System.out.println("inordered :" + inorderNodes.toString());
		return inorderNodes.get(k - 1);
	}

	public void dfsInorder(TreeNode root, List<Integer> list) {
		if (root == null) {
			return;
		}

		dfsInorder(root.left, list);
		list.add(root.val);
		dfsInorder(root.right, list);

		return;
	}

}

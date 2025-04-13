package com.shetty.code.tree;

public class Solution1 {
	  
		public static void main(String[] args) {
			 Solution1 s = new Solution1();
			 TreeNode n0 = new TreeNode(5);

			 TreeNode n1 = new TreeNode(4);
			 TreeNode n2 = new TreeNode(11);
			 TreeNode n3 = new TreeNode(7);
			 TreeNode n4 = new TreeNode(6);
			 TreeNode n5 = new TreeNode(10);
			 TreeNode n6 = new TreeNode(21);
			 n0.left = n1;
			 n1.left = n2;
			 n2.left = n3;
			 n2.right = n4;
			 n0.right = n5;
			 n5.right = n6;
//			 int sum = n1.val + n2.val + n3.val ;
//			 System.out.println("has sum :" + sum + " ," + s.hasPathSum(n0, 22));
//			 System.out.println("has good nodes :" + s.goodNodes(n0));
//			 System.out.println("maxDepth :" + s.maxDepth(n0));
//			 System.out.println("minDepth :" + s.minDepth(n0));
			 System.out.println("countNodes :" + s.countNodes1(n0));

		}

		public int countNodes(TreeNode root) {
	        if (root == null) {
	            return 0;
	        }
	        return 1 + countNodes(root.left) + countNodes(root.right);
	    }
		
		public int countNodes1(TreeNode node) {
			if (node == null) {
				return 0;
			}
			
			int left = countNodes(node.left);
			int right = countNodes(node.right);
			
			return left + right + 1;
		}
		
	int target;
    
    public boolean hasPathSum(TreeNode root, int targetSum) {
        target = targetSum;
        return dfsHasPathSum(root, 0);
    }
    
    public boolean dfsHasPathSum(TreeNode node, int curr) {
        if (node == null) {
            return false;
        }
        
        curr += node.val;
        
  //      System.out.println(node.val + ", curr=" + curr + ", target " + target);
       
        if (node.left == null && node.right == null) {
           return curr == target;
        } 
        
        boolean left = dfsHasPathSum(node.left, curr);

        boolean right = dfsHasPathSum(node.right, curr);

        return left || right;
    }
    
    public int goodNodes(TreeNode root) {
        return dfsGoodNodes(root, Integer.MIN_VALUE);
    }
    
    public int dfsGoodNodes(TreeNode node, int maxSoFar) {
        if (node == null) {
            return 0;
        }
        
        int left = dfsGoodNodes(node.left, Math.max(maxSoFar, node.val));
        int right = dfsGoodNodes(node.right, Math.max(maxSoFar, node.val));
        int ans = left + right;
       
        if (node.val >= maxSoFar) {
            ans += 1;
        }
        
        return ans;
    }
    
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        
        if (p == null || q == null) {
            return false;
        }
        
        if (p.val != q.val) {
            return false;
        }
        
        boolean left = isSameTree(p.left, q.left);
        boolean right = isSameTree(p.right, q.right);
        return left && right;
    }
    
    public int minDepth(TreeNode root) {
        return dfsMinDepth(root);
    }

    private int dfsMinDepth(TreeNode node) {
        if (node == null) {
            return 0;
        }

        if (node.left == null) {
            return 1 + dfsMinDepth(node.right);
        } else  if (node.right == null) {
            return 1 + dfsMinDepth(node.left);
        }

        int left = dfsMinDepth(node.left);
        int right = dfsMinDepth(node.right);

        return 1 + Math.min(left, right);
    }
    
    public int maxDepth(TreeNode root) {
        return dfsMaxDepth(root);
    }

    private int dfsMaxDepth(TreeNode node) {
        if (node == null) {
            return 0;
        }

        if (node.left == null) {
            return 1 + dfsMaxDepth(node.right);
        } else  if (node.right == null) {
            return 1 + dfsMaxDepth(node.left);
        }

        int left = dfsMaxDepth(node.left);
        int right = dfsMaxDepth(node.right);

        return 1 + Math.max(left, right);
    }
  
}

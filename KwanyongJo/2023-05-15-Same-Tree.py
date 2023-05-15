# Given the roots of two binary trees p and q,
# write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:

        #base case : if both trees are empty -> return true
        if p == None and q == None :
            return True

        #If one of trees is empty and the other is not empty -> return false
        elif p == None or q == None :
            return False

        # If the values of tree are not equal -> false
        elif p.val != q.val:
            return False

        #continue to judge the value the subtrees of the left and the right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    tree1_root = TreeNode(1)
    tree1_root.left = TreeNode(3)
    tree1_root.right = TreeNode(2)

    tree2_root = TreeNode(1)
    tree2_root.left = TreeNode(2)
    tree2_root.right = TreeNode(3)

    s = Solution()

    print(s.isSameTree(tree1_root, tree2_root))

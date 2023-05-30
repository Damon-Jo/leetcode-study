# Given the roots of two binary trees root and subRoot,
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree tree could also be considered as a subtree of itself.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # If t tree is none we instantly have a match
        if t is None:
            return True
        # If t isn't None and S is we don't have a match
        if s is None:
            return False
        # If any of the node values we transverse match t we check for same tree
        if s.val == t.val:
            if self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right):
                return True
        # Recurse if no match s left and right with an "OR" since only need one match
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same_tree(self, s: TreeNode, t: TreeNode) -> bool:
        # If both our none typically leaf nodes we have a match on that Node
        if s is None and t is None:
            return True
        # If one is None and the other has a value we don't have a match
        elif s is None or t is None:
            return False
        # If both values match continue to check if children also match
        if s.val == t.val:
            return self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right)


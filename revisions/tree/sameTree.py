class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # O(n) recursively check if p and q are equal and if they exist
        # base cas eif both p and q reach none nodes

        if not p and not q:
            return True

        # now we check that values exist aand equa;
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

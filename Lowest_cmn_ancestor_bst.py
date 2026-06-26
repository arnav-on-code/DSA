#LC 235
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            else:
                return root
            
#recursion method!!!

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if p.val < root.val and q.val< root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if q.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right ,p ,q)
        return root
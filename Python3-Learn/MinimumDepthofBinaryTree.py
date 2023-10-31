class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:        
        if not root:
            return 0        
        depth = 1 
        nodes = [root]
        while all(node.left or node.right for node in nodes):
            depth += 1         
            ## cast the row of nodes to the row of their child nodes
            nodes = [child for node in nodes for child in [node.left, node.right] if child]
        return depth

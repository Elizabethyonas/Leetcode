# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_path(root: TreeNode, target: int, path: List[str]) -> bool:
            if not root:
                return False
            if root.val == target:
                return True
            path.append('L')
            if find_path(root.left, target, path):
                return True
            path.pop()
            path.append('R')
            if find_path(root.right, target, path):
                return True
            path.pop()
            return False

        # Find paths from root to startValue and destValue
        start_path = []
        dest_path = []
        find_path(root, startValue, start_path)
        find_path(root, destValue, dest_path)
        
        # Find the first divergence point
        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1
        
        # Steps to go up to the common ancestor
        up_moves = 'U' * (len(start_path) - i)
        
        # Steps to go down to the destination
        down_moves = ''.join(dest_path[i:])
        
        # The result is a combination of up_moves and down_moves
        return up_moves + down_moves

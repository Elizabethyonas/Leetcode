# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        result = []

        def helper(node, is_root):
            if not node:
                return None

            is_deleted = node.val in to_delete_set

            if is_root and not is_deleted:
                result.append(node)

            node.left = helper(node.left, is_deleted)
            node.right = helper(node.right, is_deleted)

            return None if is_deleted else node

        helper(root, True)
        return result

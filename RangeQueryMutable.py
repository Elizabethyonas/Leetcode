from typing import List
class Node:
    def  __init__(self):
        self.lChild = None
        self.rChild = None
        self.left = 0
        self.right = 0
        self.sum = 0


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build(0, len(self.nums) - 1)

    def build(self, left, right):
        node = Node()
        node.left = left
        node.right = right

        if left == right:
            node.sum = self.nums[left]
            return node

        mid = (right + left) // 2
        node.lChild = self.build(left, mid)
        node.rChild = self.build(mid + 1, right)

        node.sum = node.lChild.sum + node.rChild.sum

        return node
    
    def pointUpdate(self, node, index, value):
        if node.left == node.right: # leaf node: update the sum with the value directly
            node.sum = value
            return

        mid = (node.left + node.right) // 2
        if index <= mid:
            self.pointUpdate(node.lChild, index, value)
        else:
            self.pointUpdate(node.rChild, index, value)
        
        node.sum = node.lChild.sum + node.rChild.sum

    def rangeQ(self, node, l, r):
        # case 1 when the query range is out of range
        if l > node.right or r < node.left:
            return 0

        # case 2 when the query range is completly inclusive
        if l <= node.left and r >= node.right:
            return node.sum

        # case partially covered the range
        left_sum = self.rangeQ(node.lChild, l, r)
        right_sum = self.rangeQ(node.rChild, l, r)
        return left_sum + right_sum
         

class NumArray:

    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segment_tree.pointUpdate(self.segment_tree.root, index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.rangeQ(self.segment_tree.root, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        matrix = []
        for i in range(m):
            matrix.append([-1]*n)
        
             
        arrleft = 0
        
        row,col = 0,0
        upper = 0
        bottom = m - 1
        left = 0
        right = n - 1
        t = n*m
        turn = [0,0,0,0]
        if len(matrix[0]) > 1:
            turn[0] = 1
        else:
            turn[1] = 1
        while t:
            matrix[row][col] = arr[arrleft]
            arrleft += 1
            if arrleft == len(arr):
                break
            if turn[0]:
                col+=1
                if col==right:
                    turn[0]=0
                    turn[1]=1
                    upper+=1
            elif turn[1]:
                row += 1
                if row ==bottom:
                    turn[1]=0
                    turn[2]=1
                    right-=1
            elif turn[2]:
                col -= 1
                if col==left:
                    turn[2]=0
                    turn[3]=1
                    bottom-=1
            elif turn [3]:
                row -= 1
                if row==upper:
                    turn[3]=0
                    turn[0]=1
                    left+=1
            t -= 1
            #print(left,upper,right,bottom)
        return matrix

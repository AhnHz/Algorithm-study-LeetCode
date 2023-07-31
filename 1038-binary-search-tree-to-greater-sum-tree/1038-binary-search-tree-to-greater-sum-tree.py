# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val    # 노드의 val값
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nval = 0     # 노드 이동시 추가될 누적값
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 노드가 존재한다면
        if root:    
            self.bstToGst(root.right)   # 재귀호출로 가장 오른쪽 노드부터 <--
            
            self.nval += root.val    # 노드의 val값을 이동 누적값에 누적시킴(+=자기 자신)
            root.val = self.nval     # 노드의 val값을 현재까지의 누적값으로 치환
            
            self.bstToGst(root.left)    # 재귀호출로 가장 왼쪽 노드까지 <--
            
        return root     # 총 누적값(최상위 노드 val값)
        
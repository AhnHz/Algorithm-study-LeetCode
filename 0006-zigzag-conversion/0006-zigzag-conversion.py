class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        lst = [''] * numRows
        idx, step = 0, 1

        for i in s:
            lst[idx]+=i

            if idx == 0: # 인덱스가 첫줄
                step = 1 # 아래로 이동
            elif idx == numRows-1: # 인덱스가 마지막줄
                step = -1 # 위로 이동

            idx += step # 줄 이동

        return "".join(lst)


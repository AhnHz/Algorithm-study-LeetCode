class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start = 0
        last = len(height)-1

        while start < last:

            if height[start] >= height[last]:    # 왼쪽 막대가 클 경우 -> 오른쪽 막대 기준으로 계산
                max_area = max(max_area, height[last] * (last-start))
                last -= 1   # 오른쪽 막대 이동

            else:  # 오른쪽 막대가 클 경우 -> 왼쪽 막대 기준으로 계산
                max_area = max(max_area, height[start] * (last-start))
                start += 1  # 왼쪽 막대 이동

        return max_area

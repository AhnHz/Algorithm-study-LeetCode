class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length, start = 0, 0

        for idx, val in enumerate(s):
            if val in used and used[val] >= start: # 문자열이 해시테이블에 존재하고, 기존 start 위치가 앞일 경우
                start = used[val] + 1 # 시작위치 + 1

            else:
                max_length = max(max_length, idx-start+1)

            used[val] = idx # 현재의 문자를 키로 해시테이블에 저장

        return max_length
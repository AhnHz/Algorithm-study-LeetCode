from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        mostk = Counter(nums).most_common(k)    # 가장 빈도수가 높은 k개 리스트
        
        for i in range(k):
           answer.append(mostk[i][0])   # 키,값 쌍으로 묶여있기 때문에 [i]번째 값의 [키]
           
        return answer

      
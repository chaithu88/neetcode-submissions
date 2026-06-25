from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=Counter(nums)
        top=[key for key,value in hashmap.most_common(k)]
        return top

      
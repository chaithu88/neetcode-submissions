class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        length=0
        max_length=0
        for num in numset:
            if (num-1) not in numset:
                length=0
                while (num+length) in numset:
                    length+=1
                max_length=max(max_length,length)
        return max_length
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        hash=defaultdict(int)
        for i in range(len(nums)):
            hash[nums[i]]+=1
        for i in range(len(nums)):
            if hash[nums[i]]>1:
                return True
                break
        else:
            return False
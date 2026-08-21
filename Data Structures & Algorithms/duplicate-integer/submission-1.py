class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:#using dictionary
        hashmap={}
        for i in nums:
            if i in hashmap:
                return True
            hashmap[i]=True
        return False
        
        
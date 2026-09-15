class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm={}
        n=len(nums)
        res=[]

        for num in nums:
            if num not in hm:
                hm[num]=0
            hm[num]+=1
        for num, freq in hm.items():
            if freq>n//3:
                res.append(num)
        return res

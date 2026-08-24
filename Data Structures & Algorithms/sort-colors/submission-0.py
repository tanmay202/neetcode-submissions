class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ans = []

        for i in nums:
            if i == 0:
                ans.append(i)

        for i in nums:
            if i == 1:
                ans.append(i)

        for i in nums:
            if i == 2:
                ans.append(i)

        nums[:] = ans
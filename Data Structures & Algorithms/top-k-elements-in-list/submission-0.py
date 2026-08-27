class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hm = {}
        for i in nums:
            if i not in hm:
                hm[i] = 0
            hm[i] += 1
            
        ans = []

        for i in range(k):

            # max() normally finds the largest KEY in a dictionary.
            #
            # But we don't want the largest number.
            # We want the number having the highest frequency.
            #
            # hm.get tells max() to compare the VALUES
            # instead of comparing the keys.
            #
            # Example:
            # hm = {1: 3, 2: 2, 3: 1}
            #
            # hm.get(1) -> 3
            # hm.get(2) -> 2
            # hm.get(3) -> 1
            #
            # Therefore max() returns 1 because its frequency is 3.
            max_num = max(hm, key=hm.get)

            # Add that number to our answer
            ans.append(max_num)

            # Remove it from the dictionary.
            #
            # This is important because otherwise max()
            # would find the SAME number again in the next iteration.
            del hm[max_num]


        # Return the k most frequent numbers
        return ans
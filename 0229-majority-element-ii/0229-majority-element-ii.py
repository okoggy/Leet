class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        res = []
        count = Counter(nums)
        for i in count:
            if count[i] > len(nums) // 3:
                res.append(i)
        return res
        
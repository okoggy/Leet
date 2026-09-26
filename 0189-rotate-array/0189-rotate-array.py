class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # handle k > n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)      # reverse whole array
        reverse(0, k - 1)      # reverse first k elements
        reverse(k, n - 1)      # reverse remaining elements
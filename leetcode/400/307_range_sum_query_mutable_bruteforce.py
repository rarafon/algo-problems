class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val
        

    def sumRange(self, i: int, j: int) -> int:
        s = 0
        for index in range(i, j+1):
            s += self.nums[index]
        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
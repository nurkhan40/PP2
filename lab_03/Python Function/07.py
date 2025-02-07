def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return False
    return True

nums = input("Enter a value: ")
print(f"{has_33(nums)}")
def fourSum(nums, target):
    n = len(nums)

    if n < 4:
        return []

    nums.sort()

    result = set()

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif current_sum < target:
                    left += 1

                else:
                    right -= 1

    return sorted(result)
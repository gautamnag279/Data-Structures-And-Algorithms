def printClosest(arr, brr, arrSize, brrSize, target):
    diff = float('inf')
    curr_sum = 0

    left_index = 0
    right_index = brrSize - 1
    
    pairs = None

    while left_index < arrSize and right_index >= 0:
        curr_sum = arr[left_index] + brr[right_index]
        curr_diff = abs(curr_sum - target)

        if curr_diff < diff:
            diff = curr_diff
            pairs = [arr[left_index], brr[right_index]]

        if curr_sum < target:
            left_index += 1

        else:
            right_index -= 1
            
    return pairs
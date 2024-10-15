def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
numbers = [1, 2, 4, 5, 6] 
n = 6  
missing_number = find_missing_number(numbers, n)
print(f"The missing number is: {missing_number}")

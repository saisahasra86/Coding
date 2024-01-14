def calculate_checksum(num):
    num_str = str(num)
    digits = [int(d) for d in num_str]
    min_digit = min(digits)
    max_digit = max(digits)
    checksum = sum(d for d in digits if d != min_digit and d != max_digit)
    return checksum

def sum_of_checksums(nums):
    total_checksum = sum(calculate_checksum(num) for num in nums)
    return total_checksum
n=int(input())
l=[int(i) for i in input().split()]
print(sum_of_checksums(l))




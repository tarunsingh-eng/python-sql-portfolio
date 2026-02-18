def singleNumber(A):
    n = len(A)
    ones = 0
    twos = 0
    for i in range (0, n-1):
        twos = twos ^ (ones & A[i])
        ones = ones ^ A[i]
        common_bit_mask = ~(ones & twos)
        ones &= common_bit_mask
        twos &= common_bit_mask
    return ones


numbers = [3,3,2,1,4,2,1]
result = singleNumber(numbers)
print(result)

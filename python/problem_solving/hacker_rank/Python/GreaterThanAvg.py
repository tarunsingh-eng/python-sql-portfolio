# Count Elements Greater Than Previous Average
# Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.

# Example

# Input

# responseTimes = [100, 200, 150,300]
# Output

# 2
# Explanation

# - Day 0: 100 (no previous days, skip) 
# - Day 1: 200 > average(100) = 100 → count = 1 
# - Day 2: 150 vs average(100, 200) = 150 → not greater → count = 1 
# - Day 3: 300 > average(100, 200, 150) = 150 → count = 2 Return 2.
# Input Format

# The first line contains an integer n (0 ≤ n ≤ 1000), the number of days.
# If n > 0, the next n lines contains an integer representing responseTimes[i].
# If n = 0, the second line is omitted or empty.
# Example

# 4
# 100
# 200
# 150
# 300
# here 4 is the length of array, followed by the elements of array on each line.

# Constraints

# 0 <= responseTimes.length <= 1000
# 1 <= responseTimes[i] <= 10^9 for 0 <= i < responseTimes.length
# Output Format

# A single integer depicting the count of days.
# Sample Input 0

# 0
# Sample Output 0

# 0
# Sample Input 1

# 1
# 100
# Sample Output 1

# 0

# Techniques Used to Solve the Response Time Regression Problem:

# Running Sum: Maintaining a cumulative sum of all previous elements to efficiently calculate averages without recalculating from scratch each time.

# Integer Arithmetic: Using multiplication instead of division (responseTimes[i] * i > running_sum) to avoid floating-point precision errors when comparing with averages.

# Linear Scan: Processing the array once from left to right with O(n) time complexity.

# Edge Case Handling: Properly handling the first element (which has no previous elements) and empty arrays.

# Counter Pattern: Using a simple counter variable to track the number of elements that meet our criteria.

# This approach is efficient with O(n) time complexity and O(1) space complexity, making it suitable for the given constraints where the array can have up to 1000 elements with values up to 10^9.


import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    if len(responseTimes) == 0:
        return 0 
    count = 0
    # avg = 0
    running_sum = responseTimes[0]
    for i in range (1, len(responseTimes)):
        # avg = running_sum / i
        
        if responseTimes[i] * i > running_sum:
            count +=1
        
        running_sum += responseTimes[i]
        
    return count

if __name__ == '__main__':
    responseTimes_count = int(input("Enter Response Time Number : ").strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input("Enter Responce Time ").strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)

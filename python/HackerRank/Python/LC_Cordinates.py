# Question:
# Take four integers x, y, z, n.
# Print all possible coordinates [i, j, k] such that:
# - i ranges from 0 to x
# - j ranges from 0 to y
# - k ranges from 0 to z
# - The sum i + j + k should NOT be equal to n

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

# Answer:
# Use list comprehension to generate all combinations
# and filter out those where i + j + k == n
    
print ([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range (z+1) if i+j+k !=n ])

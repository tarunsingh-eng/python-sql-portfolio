import numpy

def arrays(arr):
    b = []
    for item in arr[::-1]:
        b.append(item)
    return b
    # complete this function
    # use numpy.array

arr = [1, 2, 3, 4, -8, -10]
result = arrays(arr)
print(result)
print([f"{x:.1f}" for x in result])
print("["+" ".join(f"{x:.1f}" for x in result) + "]")
print(" ".join(f"{x:.1f}" for x in result) + " ")
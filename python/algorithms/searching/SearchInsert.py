def searchInsert(A, B):  
        l = 0
        r = len(A) - 1 
        while l <= r:
            mid = l + (r-l)//2
            print("-------------------")
            print("Value of mid is:", mid)
            print("Value of left is:", l)
            print("Value of right is:", r)
            print(int(0))
            print("-------------------")
            if A[mid] == B:
                print(mid)
                break
            elif A[mid] > B and mid == 0:
                print("0")
                break
            elif A[mid] < B and mid == len(A)-1:
                print(len(A))
                break
            elif A[mid] > B and A[mid+1] < B:
                print(mid)
                break
            elif A[mid] < B and A[mid+1] > B:
                 print(mid+1)
                 break
            elif A[mid] < B: 
                l = mid + 1
                print("left change to:", l)
            else: 
                r = mid - 1 
                print("right changed to:", r)
        print("L is now greater than R", l, r)

searchInsert ([839,841,847,859,873,877,880,886,904,909,911,993], 902)

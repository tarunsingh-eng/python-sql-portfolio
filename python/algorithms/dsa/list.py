if __name__ == '__main__':
    
    Inputs = iter([
        "12",
        "insert 0 5",
        "insert 1 10",
        "insert 0 6",
        "print",
        "remove 6",
        "append 9",
        "append 1",
        "sort",
        "print",
        "pop",
        "reverse",
        "print"
    ])

    input = lambda: next(Inputs)
    
    N = int(input())
    arr = []
 
    for _ in range(N):
        cmd = input().split()
        
        if cmd[0] == "insert":
            arr.insert(int(cmd[1]), int(cmd[2]))  
        elif cmd[0] == "print":
            print(arr)
        elif cmd[0] == "remove":
            arr.remove(int(cmd[1]))
        elif cmd[0] == "append":
            arr.append(int(cmd[1]))
        elif cmd[0] == "sort":
            arr.sort()
        elif cmd[0] == "pop":
            if arr: #make sure list if not empty
                arr.pop()
        elif cmd[0] == "reverse":
            arr.reverse()
        else:
            print("enter valid input")
            

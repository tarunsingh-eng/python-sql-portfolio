def print_formatted(number):
    # w = convert largest number to binary
    # remove 0b
    # count digits
    w = len(bin(number)[2:])
    #Print to check the width
    #print(w)

    for i in range(1, number+1):
        print(str(i).rjust(w), #print number as string justify it to right leaving the width of maximum number in binary
              oct(i)[2:].rjust(w), #print number as Octal justify it to right leaving the width of maximum number in binary
              hex(i)[2:].upper().rjust(w), #print number as Hexadecimal justify it to right leaving the width of maximum number in binary
              bin(i)[2:].rjust(w)) #print number as binary justify it to right leaving the width of maximum number in binary
    return   
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
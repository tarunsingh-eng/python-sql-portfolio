def count_substring(string, sub_string):
    count = 0
    for n in range (0, len(string)):
        if string[n:n+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ =='__main__':
    print("Enter String")
    string = input().strip()
    print("Enter Sub String")
    sub_string =input().strip()

    count = count_substring(string, sub_string)
    print(count)
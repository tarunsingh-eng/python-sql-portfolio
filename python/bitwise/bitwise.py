count = 0 
interger1 = bin(180)[2:][::-1]
for n in range(len(interger1)):
    if (interger1[n]=='0'):
        count += 1
    else: 
        break  
print(count)
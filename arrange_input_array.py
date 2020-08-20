input_str=input()
number=list(map(int,input_str))
# print(number)
# sorting the array --> keeping first element as it is and swap the adjacent elements
flag=True
for i in range(len(number)-1):
    if flag is True:
        if number[i]>number[i+1]:
            number[i],number[i+1]=number[i+1],number[i]
            
    else:
        if number[i]<number[i+1]:
           number[i],number[i+1]=number[i+1],number[i]
    flag=bool(1-flag)
print(" ".join(str(x) for x in number))
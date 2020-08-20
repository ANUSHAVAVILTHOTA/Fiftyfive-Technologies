input_str=input()
number=list(map(int,input_str))
#traversing from R->L till we find a digit which is smaller than previously traversed digit
for i in range(len(number)-1,0,-1):
    if number[i]>number[i-1]:
        #once we found that digit we will exit the traversing
        break
#if all digits are in descending order then first greater number is not possible.so printing same number
if i==1 and number[i]<=num[i-1]:
    print(input_str)

# i-1 digit is smaller than next digit
x=number[i-1]
digit_position=i
n=len(number)
# right side of i-1 position will find a smallest number which is greater than i-1 th digit
for j in range(i+1,n):
    if number[j]>x and number[j]<number[digit_position]:
        digit_position=j
number[digit_position],number[i-1]=number[i-1],number[digit_position]
x=0
#converting number upto i-1
for j in range(i):
    x=x*10+number[j]
#ascending order of digits from i-1
number=sorted(number[i:])
#converting sorted string to number
for j in range(n-i):
    x=x*10+number[j]
print(x)

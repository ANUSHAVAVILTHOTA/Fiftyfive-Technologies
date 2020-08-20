input_str=input()
split_num=[]
#splitting numbers
word=''
for char in input_str:
    if char ==' ' and word!='':
        split_num.append(word)
        word=''
    else:
        word+=char
if word!='':
    split_num.append(word)
#checking prime or not b/n interval
for num in range(int(split_num[0]),int(split_num[1]),1):
    count=0
    for i in range(2,num,1):
        if(num%i==0):
            count+=1
    if(count==0):
        print(num)

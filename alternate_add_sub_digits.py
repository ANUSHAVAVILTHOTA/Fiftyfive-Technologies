input_str=input()
# input_list=list(map(int,input()))
input_list=[]
#splitting numbers
for char in input_str:
    input_list=input_list+[int(char)]
# print(input_list)
add_sum=input_list[0]
sub_sum=0
for i in range(1,len(input_list),1):
    if(i%2==0):
        sub_sum=sub_sum+input_list[i]
    else:
        add_sum=add_sum+input_list[i]
print("Output:",add_sum-sub_sum)
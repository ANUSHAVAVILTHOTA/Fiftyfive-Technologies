n=int(input())
array=list(map(int,input()))
# print(array)
if(n==1):
    print("0")
else:
    balls=array[0]+array[1]
    total_time=array[0]+array[1]
    if(n>2):
        for i in range(2,n,1):
            balls=balls+array[i]
            total_time=balls+total_time
        print("Balls and TotalTime",balls,total_time)
    else:
        print("Balls and TotalTime",balls,total_time)
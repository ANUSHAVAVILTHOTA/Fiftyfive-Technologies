input_sent="3 2 5 6 2 7"
split_num=[]
def ResultArray(array):
    length=len(array)-1
    store=[]
    for i in range(0,length,1):
        num=array[i+1]-array[i]
        store.append(num)
    print(store)
    if(len(store)!=1):
        ResultArray(store)
    else:
        print("Output:-",store)
word=''
for char in input_sent:
    if char ==' ' and word!='':
        split_num.append(int(word))
        word=''
    else:
        word+=char
if word!='':
    split_num.append(int(word))
# print(split_num)
ResultArray(split_num)
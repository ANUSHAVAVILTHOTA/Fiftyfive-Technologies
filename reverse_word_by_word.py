input_sent=input()
split_sent=[]
word=''
for char in input_sent:
    if char ==' ' and word!='':
        split_sent.append(word)
        word=''
    else:
        word+=char
if word!='':
    split_sent.append(word)
# print(split_sent)
reverse_list=[]
for i in range(len(split_sent)-1,-1,-1):
    reverse_list.append(split_sent[i])
print("Output:",' '.join(word for word in reverse_list))

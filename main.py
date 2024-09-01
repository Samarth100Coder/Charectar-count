msg=input('Enter your message: ')
ch=input('Enter character to count: ')
count=0
for c in msg:
    if c==ch:
        count=count+1
print('Total count is: ',count)
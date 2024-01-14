stack=[]
s='leEeetcode'
for c in s:
    if(len(stack)>=1):
        if((c==chr(ord(stack[-1]) + 32))or(stack[-1]==chr(ord(c) + 32))):
            stack.pop()
            # print(c)
        else: 
            stack.append(c)
    else:
        stack.append(c)
stack=''.join([str(item) for item in stack])
print(stack)
# Upper='A'
# print(chr(ord(Upper) + 32))
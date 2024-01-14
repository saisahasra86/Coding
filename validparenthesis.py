# s='()'
# stack=[]
# n=len(s)
# for i in range(n):
#     if(s[i]=='(' or s[i]=='[' or s[i]=='{'):    
#         stack.append(s[i])
#         print(stack)
#     else:
#         if len(stack)==0: print(False)
#         c=stack[-1]
#         stack.pop()
#         if((c=='(' and s[i]==')') or (c=='[' and s[i]==']') or (s[i]=='}' and c=='{')):
#             pass
#         else:  print(False)
# if stack: print(False)
# else: print(True)
# expression='{[('
# stack=[]
# n=len(expression)
# for i in range(n):
#     if(expression[i]=='(' or expression[i]=='[' or expression[i]=='{'):
#         stack.append(expression[i])
#     else:
#         if(len(stack)==0): print("not balanced")
#         if((expression[i]==')' and stack[-1]=='(') or (expression[i]==']' and stack[-1]=='[') or (expression[i]=='}' and stack[-1]=='{')):
#                 stack.pop()
#         else:
#             print("not balanced")
# if stack: print("not balanced")
# else: print("Balanced")



# queue = []
# string = 'AB12CD34567891011'

# # Enqueue characters into the queue
# for char in string:
#     queue.append(char)
# #no.levels ka
# import math
# n=len(queue)
# numberoflevels = math.floor(math.log2(n))

# # Print the characters in the leftmost branch
# i=0
# while i<=numberoflevels:
#     character = queue[2**i-1]
#     i+=1
#     print(character)
str1='Welcome to Coding Ninjas'
n=len(str1)
string=''
stack=[]
for i in range(n):
    if str1[i]=='':
        if len(string)!=0:
            stack.append(string)
            string=''
        print(stack)
    else:  string+=str1[i]
string1=''
for i in range(len(stack)):
    string1+=stack[i]
    string1+=''
    print(string1)
print(string1)
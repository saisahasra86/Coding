s=input()
result = set()
for i in range(len(s)+1):
    for j in range( i + 1, len(s)+1):
            result.add(s[i:j]);
print(len(result))

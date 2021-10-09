# put your python code here
n = int(input())
b = str(input())
for i in range(len(b)):
    b[i] = chr(ord(b[i]) - n)
print(b)
    

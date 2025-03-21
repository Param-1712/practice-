n=int(input())
res=""
new=""
while n>0:
    res = str(n%2) + res
    n//=2
print(res)
for i in res:
    if i =='1':
        new = new+"0"
    else:
        new+="1"
final=int(new,2)
print(final)
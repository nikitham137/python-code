'''i=1
while i<=5:
    print("hello")
    i+=1
 
l=eval(input("Enter the number: "))
   
i=0
while i<len(l):
    print(l[i])
    i+=1 '''
    
'''for i in range(5):
    print("hello")
    
n=input("enter a word")
out=""
for i in n:
    if 'a'<=i<='z':
        out=out+chr(ord(i)-32)
    else:
        out=out+i
print(out)

s=[12,10,'hello','good',5j,'bye']
out={}
for i in s:
    if type(i)==str:
        out[i]=i[0]+i[-1]

print(out)

def convert(s):
    out=""
    for i in s:
        if 'a'<=i<='z':
            out=out+chr(ord(i)-32)
        else:
            out+=i
        print(out)
    print()'''
    
    
'''   
s=len("Python programming")
print(s)'''

    
'''l=input("Enter the wordr:")
out=""
for i in l:
    if 'A'<=l<='Z':
        out=out+chr(ord(i)+32)
    else:
        out=out+i
print(out)'''
        
s="good morning good afternoon good evening"
print(s.count("good"))
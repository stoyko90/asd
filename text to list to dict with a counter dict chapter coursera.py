name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict1={}
b=[]
for line in handle:
    if line.startswith("From "):
        a=line.split()
        qwe=a[1]
        b.append(qwe)
for qwe in b:
    dict1[qwe]=dict1.get(qwe,0)+1

emailsender=None
sendercount=None

for qwe,count in dict1.items():
    if sendercount is None or count>sendercount:
        sendercount=count
        emailsender=qwe

print(dict1)
print(emailsender,sendercount)










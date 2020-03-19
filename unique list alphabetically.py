fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:#check every line in the text
    a=line.split() #convert every line to a list
    for w in a:     #check every very in a line
        lst.append(w)   #add every word from the list
x=[]        #create an empty list
for i in lst:#check every item from list )
    if i not in x: #and if not in the empty list x
        x.append(i) #add it once to avoid repetativeness
x.sort() #sort alphabetically
print(x) #print out the new list x
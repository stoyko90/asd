


fname = input("Enter file name: ")  #promts user to enter manually file name and saves in fname variable
fh = open(fname)                    #opens the file the user has entered ( if it exists )
count=0                             #counter variable
d=0                                 #sum variable
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue  #ignores all line not starting with "X..."
    count = count + 1               #counts every time it sees a line that starts with "X..."
    a=line.find("0")                #finds the character number in the string that starts with 0
    b=float(line[a:])               #reads all characters starting from "0" and coverts to float
    d=d+b                           #sums up all float numbers for previous line

print("Average spam confidence:",d/count)   #prints the avg of all numbers ( sum divided by total count )

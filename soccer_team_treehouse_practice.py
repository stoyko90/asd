plist=[]
addpl=input("Would you like to add a player to the list? (yes/no) ")

while addpl=="yes":
  namepl=input("Enter the name of the player to add to the team:")
  plist.append(namepl)
  addpl=input("Would you like to add another player? (yes/no) ")

if addpl=="no":
  print("There are ",len(plist)," players on the team.")
  count = 1
  for i in plist:
    print("Player ",count,":",i)
    count+=1

gkeep=int(input("Please select the goal keeper by selecting the player number. (1-",len(plist),")"))
print("Great!!! The goalkeeper for the game will be ",plist[gkeep-1])









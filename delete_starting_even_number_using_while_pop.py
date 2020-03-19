def delete_starting_evens(lst):
    a=lst.copy()
    num=0
    while a[num]%2==0:
        if len(lst)==1:
            lst.pop(0)
            break
        else:
            lst.pop(0)
            num+=1
    return lst
#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
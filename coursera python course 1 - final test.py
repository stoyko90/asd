
largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done": break

        a=int(num)
        if smallest is None:
            smallest=a
        if a<smallest:
            smallest=a
        if largest is None:
            largest=a
        if a>largest:
            largest=a
    except:
        a=str(num)

if  num is not "done":
    print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
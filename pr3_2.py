n = int(input("enter number of elemets:"))

list1 = []
neg = []
pos = []
odd = []
even = []

print()



# get numbers from user

for i in range(n):
    list1.append(int(input(f"enter {i+1} element:")))


# check positive or negative number

for i in list1:
    if(i > 0):
        pos.append(i)
    elif(i < 0):
        neg.append(i)
    else:
        del list1[i]


# check odd-even number

for i in list1:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)

print("\n\npositive numbers")

print(pos)

print("\nnegative numbers")

print(neg)

print("\nodd numbers")

print(odd)

print("\neven numnbers")

print(even)

sum = 0

for i in list1:
    sum = sum + i

print("\naverage of all numbers:" , (sum/n))
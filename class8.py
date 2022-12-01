x=5
for i in range(x):
    for j in range(x):
        print(i,end=" ")
    print()
print("")


for i in range(x):
    for j in range(x):
        print(max(i+1,j+1,x-i,j-1),end=" ")
    print()

for i in range(x):
    for j in range(x):
        print(max(i,j),end=" ")
    print()

for i in range(x):
    for j in range(x):
        print(j,end = " ")
    print()
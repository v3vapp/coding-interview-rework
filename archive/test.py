
# find prime numbers between 1 and 100
li = []
for i in range(1,101,1):
    for j in range(2,i):
        if i%j==0:
            break
        if j == i-1:
            li.append(i)
            # print(i)


# find twin prime numbers
for x in range(len(li)-1):

    if li[x+1] -li[x] == 2:

        list_temp = []
        list_temp.append(li[x])
        list_temp.append(li[x+1])

        print(list_temp)


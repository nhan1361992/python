x = int (input("Please input your number: "))
def fact (x):
    if (x == 0):
        return 1
    return ( x * fact(x-1))

y = str(fact(x))
print(y[0])
# z = []
# for i in range(len(y)) :
#     if( i%3 == 0 ) and (i != len(y)):
#         a = ','+ y[i]
#     else
#         z.append(a)
# print (z)     
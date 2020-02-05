print ("begin")
arrs = []
for i in range(20,35) :
    if ((i%7 == 0) and (i%5 != 0)) :
        arrs.append(str(i))

print(','.join(arrs))
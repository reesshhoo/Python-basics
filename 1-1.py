l=[]
for i in range(2000,3201):
    if i%7==0:
        if i%5==0:
            pass
        else:
            l.append(str(i))

joined_list = ",".join(l)
print(joined_list)

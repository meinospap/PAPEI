r= raw_input()
j=list(r)
for i in range(len(j)-1):
    if j[i]=="!":
        j[i]=""
print ''.join(j)

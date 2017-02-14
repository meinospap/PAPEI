print "The  Harshad numbers are: "
for i in range (1,1001):
    if i<10:
        print i
    elif i<100:
        p1=i/10
        p2=i%10
        s=p1+p2
        if i%s==0:
            print i
    elif i<1000:
        p1=(i/10)/10
        p2=(i/10)%10
        p3=i%10
        s=p1+p2+p3
        if i%s==0:
            print i
    else:
        print i
print "The other numbers which are asked are: "
for i in range (1,1001):
    if i<10:
        print i
    elif i<100:
        p1=i/10
        p2=i%10
        s=p1*p2
        if s!=0:
            if i%s==0:
                print i
    elif i<1000:
        p1=(i/10)/10
        p2=(i/10)%10
        p3=i%10
        s=p1*p2*p3
        if s!=0:
            if i%s==0:
                print i

    

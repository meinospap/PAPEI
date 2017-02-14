list1= raw_input('Enter your list: ')
list1= eval(list1)
list1.remove(max(list1))
list1.remove(min(list1))
list1.remove(max(list1))
list1.remove(min(list1))
mo=float(sum(list1))/len(list1)
s=0
for i in range (len(list1)):
    s=((list1[i]-mo)**2)/float(len(list1))+s
import math
s1=math.sqrt(s)
print "This is the standard deviation",s1
    

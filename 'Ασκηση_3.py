list1= raw_input('Enter your list: ')
list1= eval(list1)
for i in range (len(list1)):
    if list1[i]==0:
        list1.remove(0)
        list1.append(0)
print list1

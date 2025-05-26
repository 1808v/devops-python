list_of_days=["sun","mon","tue","wed","thur","fri","sat"]

key="wed"

found= False
for day in list_of_days:
    if day==key:
        found=True

if found:
    print(key)
else:
    print("Not Found")

for day in list_of_days:
    if day==key:
        print("Found")
        break
    else:
        print("Not Found")

#found= False
#for day in list_of_days:
#    if day==key:
#        found=True
#
#if found:
#    print(key)
#else:
#    print("Not Found")
#

#####Algorithm
#list
#key=elemet 
#itrate the list 
#liear search 
#if found = elemet found 
#else element not found 
#stop 
#def say_hi(name):
#    print("Hi ", name)
#
#name="vivek"
#say_hi(name)

list_of_days=["sun","mon","tue","wed","thu","fri","sat"]

key="thu"

def linear_search(list_of_days,key):
    found= False
    for day in list_of_days:
        if day==key:
            found=True

    #if found:
    #    print(key)
    #else:
    #    print("Not Found")
    return found
#    for day in list_of_days:
#        if day==key:
#            print("Found")
#            break
#        else:
#            print("Not Found")

f = linear_search(list_of_days,key)

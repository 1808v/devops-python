file_obj = open('my_file.txt','r')      #open
#print(file_obj)
#print(dir(file_obj))
print(file_obj.read())      #process
file_obj.close()        #close 

try:
    file_obj_new = open('my_file2.txt','r+')
except FileNotFoundError:
    print("error handled")
    file_obj_new = open('my_file2.txt','w+')
    file_obj_new.write('hi')
    print(file_obj.read()) 
finally:
    file_obj_new.close()

print("this should print")

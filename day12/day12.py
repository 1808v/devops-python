#take multiple input 

#x,y = input('Enter two value: ').split()
#print(x, y)

#Take connditional input from user 

age_input = input('Enter the age: ')

age = int(age_input)
if age < 18:
    print('You are a child')
else:
    print('you are and adult')
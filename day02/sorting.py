#Bubble sort 

list_of_numbers=[1,2,34,45,32,-2,-1,87]
for i in range(len(list_of_numbers)):
    for j in range(len(list_of_numbers)):
        if list_of_numbers[i] < list_of_numbers[j]:
            temp=list_of_numbers[i]
            list_of_numbers[i]=list_of_numbers[j]
            list_of_numbers[j]=temp
print(list_of_numbers)    


list_of_numbers = [1, 2, 34, 45, 32, -2, -1, 87]
n = len(list_of_numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if list_of_numbers[j] > list_of_numbers[j+1]:
            list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]
print(list_of_numbers)

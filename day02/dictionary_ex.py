dict_of_items_1 = {
    "env":"dev",
    "server":"aws linux2",
    "ram":"4096",
    "cpu":"4",
    "active":True
}
dict_of_items_2 = {
    "env":"prd",
    "server":"aws linux2",
    "ram":"10240",
    "cpu":"8",
    "active":False
}
#print(dict_of_items)
#print(dir(dict_of_items))
#print(dict_of_items.items.__doc__)
#print(dict_of_items.keys.__doc__)
#print(dict_of_items.get("active"))

items = [dict_of_items_1,dict_of_items_2]
for env in items:
    for key,value in env.items():
        if key == "active" and value == True:
            print(env.values())
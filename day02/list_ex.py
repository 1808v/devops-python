list_of_name = list() #1 
#list_of_envs = []

list_of_cloud_servs = list(["aws","azure","gcp"])
list_of_envs = ["dev", "stg","prd"]
list_of_envs.append("client")
#print(type(list_of_envs))

#print(list_of_envs[2])
#print(list_of_cloud_servs)
#
#for i in list_of_envs:
#    print("Deploying to: ")
#    print(i)

#print(dir(list_of_envs))
print(list_of_envs.insert.__doc__)
list_of_envs.insert(2,"staging")
#print(list_of_envs)
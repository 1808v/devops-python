#!/usr/bin/python3
#List files in a directory
import os

dir="/home/vivek/Documents/my-learning/devops-python/day13"
files= os.listdir(dir)
print(files)
for file in files:
    print(file)
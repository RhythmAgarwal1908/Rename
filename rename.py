import os
import time

name_of_file_before_renaming= input("File Name with extension: ")

location_of_file =input("Folder Location where File is: ")

new_file_name=input("Enter the New File Name: ") 

os.rename(location_of_file+"/"+name_of_file_before_renaming,location_of_file+"/"+new_file_name)

print("Renaming.")
time.sleep(1)
print("Renaming..")
time.sleep(1)
print("Renaming...")
time.sleep(3)

print("Renaming.")
time.sleep(1)
print("Renaming..")
time.sleep(1)
print("Renaming...")
time.sleep(2)

print("File Renamed Sucessfully")
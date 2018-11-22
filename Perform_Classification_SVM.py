# 1. Gets all the images from user specified "Directory"
# 2. Performs classification on images one by one and stores the result
#       1 --> Mitosis region
#       0 ---> Non-Mitosis Region

import generate_bounding_box
import os
file_list=os.listdir('./Full_Size_Images')
for file in file_list[:]: # filelist[:] makes a copy of filelist.
    if not(file.endswith(".png")):
        file_list.remove(file)
#print(file_list)

#Now file_list is a list which contains all the PNG files.
print("length==",len(file_list)) #The count is 156 in our example...

count = 1 #To check how many images are processed.
#image_names = [] #List of images
classif_dict = {} #List of classification output

for tile in file_list:
    classif = 0
    #perform_classification(image,model)
    #print("Image name=",tile,"count=",count)
    if count%10 == 0:
        classif = 1
    classif_dict[tile] = classif
    classif = 0
    count += 1

print("dic len=",len(classif_dict))

for x, y in classif_dict.items():
  print("key=",x,"value=", y)
  if y ==1:
    generate_bounding_box.draw_bound('./Full_Size_Images/'+x)
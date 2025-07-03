# import os

# folder_path = "C:/Users/Saad/Downloads"
# liv = os.listdir(folder_path)
# ti = []
# for a in liv :
#     ti.append(a)
# print(ti)

######################
# f = open("file.txt", "r")

# print(f.read())
######################

data = data2 = ""

with open('file.txt') as fp:
    data = fp.read()
print(data)

with open('hello.txt') as fp:
    data2 = fp.read()

data += "\n"
data += data2

with open ('file2.txt', 'w') as fp:
    fp.write(data)






First_dict = { "Appareil": "Laptop", "Marque": "IBM", "Carte mère": "MSI Z490", "Carte Graphique":"GeForce RTX 3070", "RAM": "16G", "Processeur": "Intel core i7-G11", "SSD": "1 To" }
First_dict['RAM'] = "32" 
# print(First_dict)

# print(First_dict.keys())
# print(First_dict.values())
# print(First_dict)


# for x,y in First_dict.items():
#     print(x,y)

# d = {'gfg' : 4, 'is' : 2, 'best' : 5}
# print(str(d))

for n in list(First_dict.keys()):
    if n == 'Carte Graphique' or n == 'Processeur':
        # print(n)
        val = First_dict.pop(n)
        First_dict[val] = n
        

print(First_dict)
add = { "Système d’exploitation": "Windows 10"}
First_dict.update(add)
print(First_dict)

# for n in list(First_dict.keys()):
#     if n == 'Carte Graphique' or n == 'Processeur':
#         vall1 = reversed[3]
#         vall2 = reversed[5]
#         vall1 = vall2
#     print(list)



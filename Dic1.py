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

# for n in list(First_dict.keys()):
#     if n == 'Carte Graphique' or n == 'Processeur':
#         # print(n)
#         val = First_dict.pop(n)
#         First_dict[val] = n
# print(First_dict)
# add = { "Système d’exploitation": "Windows 10"}
# First_dict.update(add)
# print(First_dict)

##################

notes_eleves = { "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2, "Malak": 8.7, "Manal": 20.0, "Ahmed": 7.5,"Saad": 11.3, "Hannae": 9.8 }
dic1 = {}
dic2 = {}
for a,b in notes_eleves.items():
    if b >= 10 :
        dic1[a] = b
    else :
        dic2[a] = b
print(dic1)
print(dic2)
        







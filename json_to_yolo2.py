# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:31:28 2021

@author: LG
"""
# json load
import json
def load_json(fname):
    with open(fname, encoding = "utf 8") as f:
        json_obj =  json.load(f)
        
    return json_obj

label_yolo = load_json('A220148XX_04563.json')

# In[-] arrange to essentiatl information
value_of_label = list(label_yolo[0].values()) # key,value from json
split_point = value_of_label[10].split(',') # handle point x,y
#transpert to list
list_of_essential = [value_of_label[11],split_point[0],split_point[1],value_of_label[2],value_of_label[3]]

# In[-] write txt, list to str, save.
list_of_essential_final = ' '.join(list_of_essential)
save_to_txt = open('example.txt','w')#can put other folder. note way in front of txt
save_to_txt.write(list_of_essential_final)
save_to_txt.close()

# In[-] modeling for automate


# In[-]

#read label_yolo from txt
'''
with open('A220148XX_04563.txt','r') as file:
    label_yolo = file.readline()
'''
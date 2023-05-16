import os   
import sys
import urllib.request
import Bio
import Bio.PDB
import Bio.SeqRecord
import re

def contains_number(string):
    return any(char.isdigit() for char in string)

from Bio.PDB import PDBList

'''Selecting structures from PDB'''
pdbl = PDBList()
PDBlist2= ['2HZ6', '3P23', '4U6R', '4YZ9', '4YZC', '4YZD', '4Z7G', '4Z7H', '5HGI', '6HV0', '6HX1', '6SHC', '6URC', '6W39', '6W3A', '6W3B', '6W3C', '6W3E', '6W3K', '6XDB', '6XDD', '6XDF', '7BMK']
				 						
for i in PDBlist2:
    pdbl.retrieve_pdb_file(i,pdir='PDB')#
    
filename1 = '/home/emiraktan/Pure_project/PDB/'

ext = ('.cif')

new_file_name = []
# iterating over all files
for files in os.listdir(filename1):
    if files.endswith(ext):
        new_file_name.append(files)
        # printing file name of desired extension
    else:
        continue

resolution_list = []
new_list = []
float_list = []
LENGHT_list = []
#for i in new_file_name:
    #print(i)
for i in new_file_name:
    #print(i)
    f = open(i, "r")
    new_list = []
    found_float = False
    found_res = False
    file = f.readlines()
    f = open(i, "r")
    length = len(file)
    count =0
    for string in f:
               
        if "_refine.ls_d_res_high" in string:
            new_list = string.split(' ')
            #print(new_list)
            for i in new_list:
            
                if (contains_number(i)) == True:

                    
                    input_str = i
                    #print(input_str)
                    converted = re.findall(r'\d+\.\d+', input_str)
                    #print(converted[0])
                    new_converted = float(converted[0])
                    #print(new_converted)
                    float_list.append(new_converted)
                    #print(float_list)
                    found_float = True
                    
            if found_float == False:
                float_list.append(0)
                found_res = True

                #i += resolution_list
        count += 1
        
        if count == length-1 and not found_float and not found_res:
            float_list.append(-1)
           
dictionary = {}

for i in new_file_name:
    #print(i)
    f = open(i, "r")
    new_list = []
    UniProt = False
    file = f.readlines()
    f = open(i, "r")
    #length = len(file)
    count = 0
    check = False
    seq = []
    for string in f:
        if check:
            #print(string)
            string = string.strip()
            seq.append(string)
            if string == "#":
                check = False
            
        
        if '_struct_ref_seq.pdbx_auth_seq_align_end' in string:
            a = string.strip()
            seq_len = a[39:].strip()
            if contains_number(seq_len) == True:
                #print(seq_len) 
                dictionary[i] = int(seq_len)
            
            

            else:
                #print("yok")
                check = True
    #print(seq)
    seq = seq[:-1]

    for strq in seq:
        strq = strq.split("?")
        a = strq[2]
        #print(a)
        if "O75460" in strq[2]:
            seq_len = strq[1].strip()
            #print(seq_len)
            dictionary[i] = int(seq_len)
            break

#print(dictionary)

    
            
    


"""
        while check:
            if string == ";\n":
                check = False
                break

            seq += string
"""
"""
        if "_struct_ref.pdbx_db_accession" in string:
            new_list = string.split(' ')
            #print(new_list)
            for i in new_list:
                if i == 'P05067':
                    UniProt = True
                    print("yes")
                    break
                else:
                    UniProt = False                
"""
        
                    




            
#print(new_file_name)


"""
print(float_list)
print(new_file_name)
print(len(float_list))
print(len(new_file_name))
"""
for i in range(len(float_list)):
    if float_list[i] < 3.00 and float_list[i] > 0:
        print(new_file_name[i], "is valid:", float_list[i] )
    elif float_list[i] >= 3.00:
        print(new_file_name[i], "is invalid:", float_list[i] )
    elif float_list[i] == 0:
        print(new_file_name[i], "is unknown and E-microscopy:", float_list[i])
    elif float_list[i] == -1:
        print(new_file_name[i], "is NMR:", float_list[i])

"""
for i, pdb_id in zip(float_list, new_file_name):
    if i < 3.00:
        print(pdb_id, "is valid:", i)
    elif i >= 3.00:
        print(print(pdb_id, "is invalid:", i))
"""
print("                                                                                                                     /n -----------------------------------------------------------------------------------------------------------------------                                                                                                    ")

for key, val in dictionary.items():
    if val < 100:
        print(key, ": invalid")
    elif val >= 100:
        print(key, ": valid")

print("                                                                                                                     /n -----------------------------------------------------------------------------------------------------------------------                                                                                                    ")   


    
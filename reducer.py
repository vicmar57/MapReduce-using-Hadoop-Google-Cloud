# -*- coding: utf-8 -*-
"""
@author: Victor Martinov, Eran Hoffman
"""
import sys
#for_reduce = open("for_reduce.txt","r") 
#out = open("output.txt","a") 

for line in sys.stdin:
#for line in for_reduce:
#    print(line.strip())
    stu_id, stu_firstname, stu_lastname, stu_birth_date, g1, g2 , g3 = line.split()
    if(int(stu_birth_date) > 1990 and int(g1) > 80 and int(g2) <= 95):
        print(line)
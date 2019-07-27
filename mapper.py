# -*- coding: utf-8 -*-
"""
@author: Victor Martinov, Eran Hoffman
"""

def read_cache():
    with open('ref') as f:
        for line in f:
#            print(line.strip())
            key, val1, val2, val3 = line.strip().split(",")
            vals = [val1, val2, val3]
#            print("key:", key, "val:" , vals)
            stu_grade_dict[key] = vals
			
import sys
stu_grade_dict = {}
read_cache()

for line in sys.stdin:
#for_reduce = open("for_reduce.txt","a") 
#with open("student_small_50000.txt") as f:
    #for line in f:
        #print(line.strip().split(','))
    stu_id, stu_name, stu_birth_date = line.strip().split(',')
    if(stu_id in stu_grade_dict):
        string = "%s %s %s %s %s %s" % (stu_id, stu_name, stu_birth_date, 
                                          stu_grade_dict[stu_id][0], 
                                          stu_grade_dict[stu_id][1], 
                                          stu_grade_dict[stu_id][2])
        print(string)
            #for_reduce.write(string + "\n")
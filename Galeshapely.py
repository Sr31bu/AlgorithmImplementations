#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:04:01 2023

@author: shashankramachandran
"""

import sys
import time
import pdb


def read_prefs(pref_1_filename, pref_2_filename):
    # For parts 1 an 2.
    # This function reads preferences from two files
    # and returns two-dimensional preference lists and the length, N, of the lists.
    with open(pref_1_filename, 'r') as f:
        hospital_raw = f.read().splitlines()
    with open(pref_2_filename, 'r') as f:
        student_raw = f.read().splitlines()
    N = int(student_raw[0])
    hospital_prefs = [[int(id) for id in  x.split(',')] for x in hospital_raw[1:]]
    student_prefs = [[int(id) for id in  x.split(',')] for x in student_raw[1:]]
    return N,  hospital_prefs, student_prefs

def read_prefs_q3(com_pref_file, stu_pref_file):
    # This function reads preferences from two files (the first for companies, the second for students)
    # and returns two-dimensional preference lists and the parameters N, M and k.
    with open(com_pref_file, 'r') as f:
        company_raw = f.read().splitlines()
    with open(stu_pref_file, 'r') as f:
        student_raw = f.read().splitlines()
    N = int(student_raw[0])
    parameters = [int(x) for x in company_raw[0].split(',')]
    M = parameters[0]
    k = parameters[1]
    student_prefs = [[int(id) for id in  x.split(',')] for x in student_raw[1:]]
    company_prefs = [[int(id) for id in  x.split(',')] for x in company_raw[1:]]
    return N, M, k, company_prefs, student_prefs

def inverse_prefs(N,prefs):
    ranks = [[None for i in range(N)] for i in range(N)]
    for hospital in range(N):
        for student in range(N):
            student_prefs = prefs[hospital][student]
            ranks[hospital][student_prefs] = student
    return ranks 

def inverse_prefs_intern(N,M,prefs):
    ranks = [[None for i in range(M)] for i in range(N)]
    for company in range(N):
        for student in range(M):
            student_prefs = prefs[company][student]
            ranks[company][student_prefs] = student
    return ranks 

    
   
def curr_match(N,matchings):
    matching_ranks = N * [None]
    for i in range(N):
        matching_ranks[matchings[i][1]] = matchings[i][0]
        
    return matching_ranks

def run_GS(N, hospital_prefs, student_prefs, out_name):
    free_hospital = list(range(N)) # This list will be used as a stack
                                   # (because Python lists provide O(1)-time stack operations).
    count = N*[0] # stores the index of each hospital's next unproposed student, 
                  # going from the left of hospital's preference list   
    job = N*[None] # Stores the hospital currently matched to each student.
    
    student_ranks = inverse_prefs(N,student_prefs)
    print(student_prefs)
    print(student_ranks)

    # Gale-Shapley algorithm with hospitals making offers to students
    while free_hospital:  # returns True if list is nonempty
        hospital = free_hospital.pop() # Remove the hospital on top of the stack.  
        student = hospital_prefs[hospital][count[hospital]] #which student does the hospital propose to 
        # print(hospital, 'proposing to', student)
        count[hospital] += 1
        if job[student] is None:   # student is not paired 
            job[student] = hospital
            # print('student is not paired')
            
        else:
            if student_ranks[student][hospital] < student_ranks[student][job[student]]: #prefers the fiance to the currently married match 
                ##pdb.set_trace()
                hospital2 = job[student] # the old  match becomes the new hospital 
                free_hospital.append(hospital2)
                job[student] = hospital
            else:
                 #student regcts the hosptial so we add it 
                free_hospital.append(hospital)
    # write matches to output file
    with open(out_name, 'w') as f:
        for student, hospital in enumerate(job):
            f.write(str(hospital)+','+str(student)+'\n')
    return job # In addition to writing the output to a file, this code returns a list of jobs given to each student. You can use this for testing. 


#explanation of the code that I have added. If the hospital we are currently looking at is preferred by a student compared 
# to the students match we can say that we match the hospital to this new student and remove the old match. Otherwise the 
#match is rejected.  



############################################################
# PART 2 STARTER CODE
############################################################

def check_stable(N, hospital_prefs, student_prefs, match_file):
    student_rank = inverse_prefs(N,student_prefs)
    hospital_rank = inverse_prefs(N,hospital_prefs)
    perfect_match_hos= N * [0]
    perfect_match_stu= N * [0]
    with open(match_file,'r') as f:
        matchings = [[int(id) for id in pair.split(',')] for pair in f.read().splitlines()]
    ########################################
    # Your code goes here!
    #######################################
    stable_and_perfect = True
    resident_match = curr_match(N,matchings)
    for i in range(N):
        h = matchings[i][0]
        # stores the  hospital number we are using 
        r = matchings[i][1]
        # sotres the resident number that matches hospital h 
        perfect_match_hos[h] +=1
        perfect_match_stu[r] +=1
        if(perfect_match_hos[h]!= 1 and perfect_match_stu[r] != 1):
            stable_and_perfect = False
        for j in range(N):   
            # iterates over the hospitals array
            if (hospital_rank[h][j] < hospital_rank[h][r]) and (student_rank[j][h]  < student_rank[j][resident_match[j]]):
                stable_and_perfect = False

    if stable_and_perfect  : 
        print(1)     # if stable
    else:
        print(0)     # if not stable
    return stable_and_perfect

#explanation of the code. We have out standard inverse preference lists. We use an array to see if the matching is perfect 
#by checking if a company is matched to more that one student or not and vice versa. Then we check for stability by 
# seeing if the hospital or the student prefer someting else compared to its current match. If any case meets this case we
# return false and print 1
    
############################################################
# PART 3 STARTER CODE
############################################################
def find_stable_intern_assignment(N,M,k, company_prefs, student_prefs, out_name):
    
    job = N*[None] # for each student, job[i] is the company they are currently matched to
    NoofInterns = M * [0] # stores the number of interns a company has
    free_company = list(range(M)) # the stack for the company 
    count = M*[0] #stores the index of the student the company hasnt proposed to
    student_ranks = inverse_prefs_intern(N,M,student_prefs) #generates the normal preference arrayfor the student
    company_ranks = inverse_prefs_intern(M,N,company_prefs) #generates the normal preference array for the company 
    while free_company:
        company = free_company[-1] #takes the first company out of the stack
        print(company,NoofInterns[company])
        if(NoofInterns[company]==k or count[company]==N):#if the No of Interns of a company is equivalent to k  or has the compnay proposed to all the students 
            free_company.pop() # freecompany.pop() removes the company since it is already paired to k or proposed to all the students  
            continue
        student = company_prefs[company][count[company]] # which student does the company propose to? 
        count[company] += 1 #count[company] increases by 1
        if job[student] is None:  
            # student is not paired 
            job[student] = company 
            NoofInterns[company] += 1
        else:
            if student_ranks[student][company] < student_ranks[student][job[student]]: #prefers the fiance to the currently married match 
                ##pdb.set_trace()
                company2 = job[student] # the old  match becomes the new hospital 
                NoofInterns[company2] -= 1
                job[student] = company #the new match is the company we are looking at 
                NoofInterns[company] += 1
                if(company2 not in free_company):
                    print("inhere ")
                    free_company.append(company2)
    with open(out_name, 'w') as f: 
        for student, company in enumerate(job):
            f.write(str(company)+','+str(student)+'\n')
    return job

#explanation of the code three is a similar to Gale-Shapely algoritm. It follows the same steps like convertinng 
# the inputs to inverse preference lists and stuff but the only difference is that I used an array to store a count of the 
#number of interns a company could have. Then I popped an element out of the stack when a company hired k interns. The main 
# idea of this code is the ability to store multiple items and this was done using an array. I also used the better efficieny 
# O(MN) compared to 0(MNK). Comments are added for understanding the code better. 
                    
   

   
            

def main():
    # Do not modify main() other than using the commented code snippet for printing 
    # running time for Q1, if needed
    if(len(sys.argv) < 5):
        return "Error: the program should be called with four arguments"
    hospital_prefs_file = sys.argv[1] 
    student_prefs_file = sys.argv[2]
    match_file = sys.argv[3]
    # NB: For parts 1 and 3, match_file is the file to which the *output* is wrtten
    #     For part 2, match_file contains a candidate matching to be tested.
    question = sys.argv[4]
    N, hospital_prefs, student_prefs = read_prefs(hospital_prefs_file, student_prefs_file)
    if question=='Q1':
        # start = time.time()
        run_GS(N, hospital_prefs,student_prefs,match_file)
        # end = time.time()
        # print(end-start)
    elif question=='Q2':
        check_stable(N, hospital_prefs, student_prefs, match_file)
    elif question=='Q3':
        company_prefs_file = hospital_prefs_file
        N, M, k, company_prefs, student_prefs = read_prefs_q3(company_prefs_file, student_prefs_file)
        find_stable_intern_assignment(N, M, k, company_prefs, student_prefs, match_file)
    else:
        print("Missing or incorrect question identifier (the fourth argument should be \'Q1\', \'Q2\', or \'Q3\', without quotes).")
    return

if __name__ == "__main__":
    # example command: python stable_matching.py pref_file_1 pref_file_2 match_name Q1
    
    # stable_matching.py: filename; do not change this
    # pref_file_1: filename of the first preference list
    # pref_file_2: filename of the second preference list
    # match_name: desired filename for output (or input, for Q2)  matching file
    # Q1: desired question for testing. Can be Q1, Q2, or Q3.
    main()
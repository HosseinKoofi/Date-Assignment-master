#!/usr/bin/env python3
''' template for date assignment script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
Program: a1_[student_name].py (replace [student_name] with your student name)
Author: "Student Name"
The python code in this file (a1_[student_name].py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource.
'''
import os
import sys

def leap_year(obj):
    '''
    put your function level docstring here ...
    '''
    ...

    return status

def sanitize(obj1,obj2):
    '''
    put your function level docstring here ...
    '''
    ...
    
    return results

def size_check(obj, intobj):
    '''
    put your function level docstring here ..
    '''
    ...

    return status

def range_check(obj1, obj2):
    '''
    put your function level docstring here ..
    '''
    ...
    
    return status
    
def usage():    
    '''
    put your function level docstring here ...
    '''
    ...
    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   #print('Sanitized user data:', dob)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print(new_dob)  

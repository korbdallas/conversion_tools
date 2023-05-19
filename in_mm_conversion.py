###########################################################################
## this tool is used to convert mm to inches or inches to mm
##
##       python dev_zero_client.py <server_ip> <port>
##
## Author: Michael Colombo
## Date: 5/19/2023 
##
############################################################################

#!/bin/env/python

import sys

global inches
global mm

inches=0
mm=0

def in_mm():
    inches=input("Please specify inches in decimal to convert to mm \t")
    try:  # checks if input is numeric
        inches = float(inches)
    except:
        print("Please enter values greater than 0. ")
        pass
        in_mm()
    if float(inches) < 0:
        print("Please enter values greater than 0. ")
        in_mm()
    else:
        pass
     
    mm_conversion= (inches * 25.4)
    print(inches, "inches is equal to", round(mm_conversion, 3), "mm")
    quit()
    
def mm_in():
     mm=input("Please specify mm in decimal to convert to inches \t")
     try:  # checks if input is numeric
        mm = float(mm)
     except:
        print("Please enter values greater than 0. ")
        pass
        mm_in()
     if float(mm) < 0:
        print("Please enter values greater than 0. ")
        mm_in()
     else:
        pass
     
     in_conversion= (mm / 25.4)
     print(mm, "mm is equal to", round(in_conversion, 2), "inches")
     quit()
    
def select_conversion():
    while True:
        conversion_type = input("Select conversion type, 1) inches to mm 2) mm to inches \t")
        if conversion_type == "1":
            return in_mm()
        elif conversion_type == "2":
            return mm_in()
        else:
            print("Invalid response\n")
            select_conversion()


select_conversion()

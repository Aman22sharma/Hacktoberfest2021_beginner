## AUTHOR: Andy-Ra
## GITHUB: https://github.com/Andy-Ra/
## Python3 Concept: Matrix calculator in python

import re


repeat = 'Y'
while (repeat == 'Y' or repeat == 'y'): 
  print ("++++++ WELCOME TO MATRIX CALCULATOR ++++++")

  repeat_cm = 'Y'
  while (repeat_cm == 'Y' or repeat_cm == 'y'): 
    print ("")
    ##To Insert a order matrix
    print ("")
    print ("Please input the same order matrix : ")
    fc = int(input("First order matrix row : "))
    fr = int(input("First order matrix collumn : "))
    sc = int(input("Second order matrix row : "))
    sr = int(input("Second order matrix collumn : "))
    fm = fc * fr
    sm = sc * sr

    print ("Please choose one of the commands :")
    print ("1. matrix addition")
    print ("2. matrix subtraction (coming soon)")
    choose = input("Number :")

    if (choose == "1"): ##or choose == "2"
      if (fc == sc) & (fr == sr):
        print ("")
        print ("+++++++++++++++++++++++++++++++++++++++")
        print ("Enter {} Value of First Matrix :" .format(fm))
        f_row = []
        for a_value in range (0, fc):
          f_contents = []
          for b_value in range (0, fr):
              f_number = int(input("Input index of [{}] [{}] from first matrix : ".format(a_value, b_value)))
              f_contents.append(f_number)
          f_row.append(f_contents)
        
        f_contents ='\n'.join (str(f) for f in f_row)
        print ("")
        print ("+++++++++++++++++++++++++++++++++++++")
        print ("Value of First Matrix : \n{}" .format(f_contents))

        print ("")
        print ("+++++++++++++++++++++++++++++++++++++++")
        print ("Enter {} Value of Second Matrix :" .format(sm))
        s_row = []
        for c_value in range (0, sc):
          s_contents = []
          for d_value in range (0, sr):
              s_number = int(input("Input index of [{}] [{}] from Second matrix : ".format(c_value, d_value)))
              s_contents.append(s_number)
          s_row.append(s_contents)

        s_contents ='\n'.join (str(s) for s in s_row)
        print ("")
        print ("+++++++++++++++++++++++++++++++++++++")
        print ("Value of Second Matrix : \n{}" .format(s_contents))
        

        ##if user chose matrix addition
        if (choose == "1"):
          m_row =[]
          r_row = []
          for l in range (0, len (f_row)):
            r_content = []
            for m in range (0,len (f_row [0])):
                result = int((f_row[l][m] +  s_row[l][m]))
                r_content.append(result)
              
            r_row.append(r_content)
          r_content ='\n'.join (str(h) for h in r_row)
          print ("")
          print ("+++++++++++++++++++++++++++++++++++++")
          print ("")
          print ("sum of Matrix : \n{} \n+ \n{} \n= \n{}" .format(f_contents, s_contents, r_content))

          ##to show sum method
          print ("Method :")
          for l in range (0, len (f_row)):
            m_content=[]
            for m in range (0,len (f_row [0])):
                process = ('[{} + {}]' .format(f_row[l][m],s_row[l][m]))
                m_content.append(process)

            m_row.append (m_content)
          m_content = '\n' .join (str(proc) for proc in m_row)
          print (m_content)
          
          repeat_cm = 'N'
    
        ##if user chose matrix subtaction    
        elif (choose == "2"):
          print ("coming soon")
          repeat_cm = 'N'

      else :
        print ("please insert the same order matrix")

    ##to repeat if the user choose another
    elif not (re.match("[0-9]", choose)):
      repeat_cm = 'Y'


  repeat_yn = 'Y'
  while (repeat_yn == 'Y' or repeat_yn == 'y'): 
    repeat_yn = input("Try Again? [Y/N] ")

    ## if user choose "N" option, then the program will be stopped
    if repeat_yn == 'N' or repeat_yn == 'n':
      print ("")
      print ("++++++ THANK YOU ++++++")  
      print ("+++++++++++++++++++++++++")
      repeat = 'N'

    ##if user choose "Y" option, then the program will be looping from the beginning
    elif repeat_yn == 'Y' or repeat_yn == 'y':
      repeat_yn = 'N'
      repeat = 'Y'
      
    ## If users didn't choose Y/N, this program is looping to ask "Try again" again
    else :
      repeat_yn = 'Y'
// AUTHOR: Dev Gupta
// Python3 Concept: using covid19dh library to get data
// GITHUB: https://github.com/guptadev21

//Add your python3 concept below

from covid19dh import covid19
import datetime

a, data = covid19(raw = True, verbose = False)

country = input("For which country you want the data: \n")

a, data = covid19(country, cache = False, verbose = False, start = datetime.date(2021,10,1))


#print(data.columns) #shows no. of total columns that can be accessed
#print(data)    #to show all the data
print(data.iso_alpha_3) # to show only country and no. of cases

"""

Authors: Me
Start: 3.14.2021
Last Push: 3.14.2021
Description: Solution to the Staircase problem

"""

# import
from datetime import datetime
import math

# variables
start_time = datetime.now()
input = 10
final = 0
output = []


#function for finding 2 number combonations for int
def split(start,tiles,shift):
  out = []
  for i in range(start,math.ceil(tiles/2)):
    if(shift!=[]):
      out.append(shift+[i,tiles-i])
    else:
      out.append([i,tiles-i])
  return out


#function for returning popped list
def returnpopped(myList):
  myList.pop()
  return myList

  


output = (split(1,input,[]))
splitPrevAppend = []
final = final+len(output)
#print(output)
print("----------------------")


#loop through every # of possible steps
for j in range(2):
  #loop through every # of possible first nums in step
  for i in range(len(output)):
    #split last element of output 
    #make sure to set start limit to 2nd last element of output
    splitPrev = split(output[i][len(output[i])-2]+1,output[i][len(output[i])-1],returnpopped(output[i]))

    if(splitPrev != []):
      #print(splitPrev)
      final = final + len(splitPrev)
    splitPrevAppend = splitPrevAppend + splitPrev

  print("----------------------")
  output=splitPrevAppend



#Print Answer
print("\n\n----------------------\nFINAL VALUE IS: " + str(final) + "\n----------------------\n")

# timer  
time_elapsed = datetime.now() - start_time
print('Time elapsed is {}'.format(time_elapsed))


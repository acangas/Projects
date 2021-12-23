# Project 2 - Elections
#
# Name: Anthony Cangas
# Instructor: Mork

def get_votes():
   votes =int(input('Enter number of votes: '))
   j = []
   for i in range(votes):
    v = input('Vote '+str(1+i)+': ').split()
    j.append(v)
   

   return j

def top_votes_for(name, votes):
   count = 0
   for i in range(len(votes)):
    if votes[i][0] == name:
     count = count+1
   return count

def top_two_votes_for(name, votes):
   count = 0
   for i in range(len(votes)):
    if votes[i][0] == name or votes[i][1] == name:
     count = count+1
   return count

def place_votes(name, votes):
   count = 0
   for i in range(len(votes)):
      if votes[i][0] == name:
         count = count+3
      elif votes[i][1] == name:
         count = count+2
      elif votes[i][2] == name:
         count = count+1
      else:
         count = count
   return count

def total_points_for(name, votes):
   count = 0
   for i in range(len(votes)):
    if votes[i][0] == name:
     count = count+3
    elif votes[i][1] == name:
     count = count+2
    elif votes[i][2] == name:
     count = count+1
   return count


def eliminate_no_votes(list):
   newList = []
   for i in range(len(list)):
      if list[i][1] != 0:
         newList.append(list[i])
   return newList




def tally_by_winner(names, list):
   newList = []
   for i in range(len(names)):
      count = top_votes_for(names[i],list)
      newList.append((names[i],count))

   return newList


def tally_by_place(names, list):
   newList = []
   for i in range(len(names)):
      count = place_votes(names[i],list)
      newList.append((names[i],count))
   return newList
# TODO: finish the functions above and then add in the rest

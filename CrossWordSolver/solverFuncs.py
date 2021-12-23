#Project 3 - Wordsearch
#
#Name: Anthony Cangas
#Instructor: Mork

def read_puzzle():
   search = input()
   newList = []
   for i in range(0,91,10):
      newList.append(search[i:i+10])
   return newList

def read_words():
   words = input().split()
   return words

def searcherf(list, word):
   if list.find(word) != -1:
      ans = (list.find(word),0)
   elif list[::-1].find(word) != -1:
      ans = (list[::-1].find(word),1)
   else:
      ans = (-1,-1)
   return ans

def are_same(list1,list2):
   newList = []
   for j in range(len(list1)):
      if list1[j] ==((-1,-1,-1)) and list2[j] == ((-1,-1,-1)):
         newList.append((-1,-1,-1))
      elif list1[j] == (-1,-1,-1) and list2[j] != (-1,-1,-1):
         newList.append(list2[j])    
      elif list2[j] == (-1,-1,-1) and list1[j] != (-1,-1,-1):
         newList.append(list1[j]) 
   return newList 

def print_puzzle(puzzle):
   print('Puzzle:'+'\n')
   for i in range(len(puzzle)):
      print(puzzle[i])
   print(' ')

def print_out(list,words):
   for i in range(len(list)):
      if list[i][2] == 0:
         print(words[i]+':'+' (FORWARD) '+'row: '+str(list[i][0])+
            ' column: '+str(list[i][1]))
      elif list[i][2] == 1:
         print(words[i]+':'+' (BACKWARD) '+'row: '+str(list[i][0])+
            ' column: '+str(list[i][1]))
      elif list[i][2] == 2:
         print(words[i]+':'+' (DOWN) '+'row: '+str(list[i][0])+
            ' column: '+str(list[i][1]))
      elif list[i][2] == 3:
         print(words[i]+':'+' (UP) '+'row: '+str(list[i][0])+
            ' column: '+str(list[i][1]))
      else:
         print(words[i]+': word not found')

def search_rows(puzzle,word):
   for i in range(len(puzzle)):
      ans = searcherf(puzzle[i],word)
      if ans[1] == 0:
         return (i,ans[0],0)
      elif ans[1] ==1:
         return (i,abs(ans[0]-9),1)
      else:
         tup = (-1,-1,-1)
   return tup 

def make_cols(puzzle, col):
   newList = []
   for i in range(len(puzzle)):
      newList.append(puzzle[i][col])
   return ''.join(newList)
   
def searcherc(list, word):
   if list.find(word) != -1:
      ans = (list.find(word),2)
   elif list[::-1].find(word) != -1:
      ans = (list[::-1].find(word),3)
   else:
      ans = (-1,-1)
   return ans

def search_cols(puzzle,word):
   for i in range(len(puzzle[0])):
      col = make_cols(puzzle,i)
      ans = searcherc(col,word)
      if ans[1] == 2:
         return (ans[0],i,2)
      elif ans[1] == 3:
         return (abs(9-ans[0]),i,3)
      else:
         tup = (-1,-1,-1)     
   return tup             
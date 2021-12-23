# Project 2 - Elections
#
# Name: Anthony Cangas
# Instructor: Mork

from solverFuncs import *
def main():

   votes = get_votes()

   how = input('\nHow would you like to analyze the results?\n'+
   	'(t)op votes, top t(w)o votes, t(o)tal points\n'+
   	't(a)lly by winner, tally by (p)lace, (q)uit\n')

   while how != 'q':
      if how == 't':
         name = input('Name: ')
         print('\nTop votes for '+name+':\n'+ str(top_votes_for(name, votes)))
      elif how == 'w':
         name = input('Name: ')
         print('\nTop two votes for '+name+':\n'+ str(top_two_votes_for(name, votes)))
      elif how == 'o':
      	 name = input('Name: ')
      	 print('\nTotal votes for '+name+':\n'+str(total_points_for(name, votes)))
      elif how == 'a':
         names = input('Names:\n').split()
         if input('Eliminate zero (y or n)?\n') == 'y':
            x = tally_by_winner(names,votes)
            x = eliminate_no_votes(x)
            print('\nTallies:')
            for i in range(len(x)):
               winner = x[i][0]
               tally = x[i][1]   
               print(winner+' '+str(tally))
         else:
            print('\nTallies:')
            x = tally_by_winner(names,votes)
            for i in range(len(x)):
               winner = x[i][0]
               tally = x[i][1]   
               print(winner+' '+str(tally))      
      elif how == 'p':
         names = input('Names:\n').split()
         if input('Eliminate zero (y or n)?\n') == 'y':
            x = tally_by_place(names,votes)
            x = eliminate_no_votes(x)
            print('\nTallies:')
            for i in range(len(x)):
               winner = x[i][0]
               tally = x[i][1]
               print(winner+' '+str(tally))
         else:
            x = tally_by_place(names, votes)
            print('\nTallies:')
            for i in range(len(x)):
               winner = x[i][0]
               tally = x[i][1]
               print(winner+' '+str(tally))   
      how = input('\nHow would you like to analyze the results?\n'+
   	  '(t)op votes, top t(w)o votes, t(o)tal points\n'+
   	  't(a)lly by winner, tally by (p)lace, (q)uit\n') 



if __name__ == '__main__':
	main()
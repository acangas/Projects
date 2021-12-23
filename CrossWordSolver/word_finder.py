#Project 3 - Wordsearch
#
#Name: Anthony Cangas
#Instructor: Mork
from solverFuncs import *
def main():
   puzzle = read_puzzle()
   words = read_words()
   ansr = []
   ansc = []
   for i in range(len(words)):
      ansr.append(search_rows(puzzle,words[i]))
      ansc.append(search_cols(puzzle,words[i]))
   newList = are_same(ansr,ansc)
   print_puzzle(puzzle)
   print_out(newList,words)
if __name__ == '__main__':
	main()
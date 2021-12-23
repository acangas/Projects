#Anthony Cangas
#Mork
#Proj 4
class Vote:
   '''A class to model a vote
   attributes: f,s and t'''
   def __init__(self,f,s,t):
      self.f = f
      self.s = s
      self.t = t
   def __eq__(self,other):
      return self.f == other.f and self.s == other.s\
      and self.t == other.t


class Tally:
   '''A class to model a tally
   attributes: name, count'''
   def __init__(self,name,count):
      self.name = name
      self.count = count
   def __eq__(self,other):
      return self.name == other.name and self.count == other.count
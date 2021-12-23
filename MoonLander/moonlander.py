# Project 1 - Moonlander
#
# Name: Anthony Cangas 
# Instructor: Mork

from landerFuncs import *
def main():

   showWelcome()
   ialt = getAltitude()
   ifuel = getFuel()
   print('\nLM state at retrorocket cutoff')
   velocity = 0
   time = 0
   fuelrate = 0

   while  ialt>0 and ifuel > 0:

      displayLMState(time, ialt, velocity, ifuel, fuelrate)
      fuelrate = getFuelRate(ifuel)
      acl = updateAcceleration(1.62, fuelrate)
      ialt = updateAltitude(ialt, velocity, acl)
      velocity = updateVelocity(velocity,acl)
      ifuel = updateFuel(ifuel, fuelrate)
      time = time+1

   while ialt>0 and ifuel <= 0:
   
      Oof = 'OUT OF FUEL - Elapsed Time:'
      Oof1 ='Altitude:'
      Oof2 = 'Velocity:'
      fuelrate = 0 
      print('%28s%4d %9s%8.2f %9s%8.2f' % (Oof, time, Oof1, ialt, Oof2, velocity))
      acl = updateAcceleration(1.62, 0)
      ialt = updateAltitude(ialt, velocity, acl)
      velocity = updateVelocity(velocity, acl)
      time = time+1

   if ialt <= 0:

      print('\nLM state at landing/impact')
      displayLMState(time, ialt, velocity, ifuel, fuelrate)
      displayLMLandingStatus(velocity)

if __name__ == '__main__':
	main()
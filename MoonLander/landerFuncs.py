# Project 1 - Moonlander
#
# Name: Anthony Cangas 
# Instructor: Mork 

def showWelcome():

   print('\nWelcome aboard the Lunar Module Flight Simulator'+
         '\n\n   '+"To begin you must specify the LM's initial"+
         " altitude"+'\n   '+'and fuel level.  To simulate the actual'+
         ' LM use'+'\n   '+'values of 1300 meters and 500 liters, respectively.'+
         '\n\n   '+'Good luck and may the force be with you!\n')
   
def getFuel():

   fuel = int(input('Enter the initial amount of fuel on board the LM (in liters): '))
   while fuel <= 0:
      print('ERROR: Amount of fuel must be positive, please try again')
      fuel = int(input('Enter the initial amount of fuel on board the LM (in liters): '))
   return fuel

def getAltitude():

   altitude = int(input('Enter the initial altitude of the LM (in meters): '))

   while altitude < 1 or altitude > 9999:
      print('ERROR: Altitude must be between 1 and 9999, inclusive, please try again')
      altitude = int(input('Enter the initial altitude of the LM (in meters): '))
   return altitude

def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):

   s1 = 'Elapsed Time:'
   s2 = 'Fuel:'
   s3 = 'Rate:'
   s4 = 'Altitude:'
   s5 = 'Velocity:'
   print('%13s %7d s' % (s1,elapsedTime))
   print('%13s %7d l' % (s2, fuelAmount))
   print('%13s %7d l/s' % (s3, fuelRate)) 
   print('%13s %7.2f m' % (s4, altitude))
   print('%13s %7.2f m/s' % (s5, velocity))

def getFuelRate(currentFuel):

   fuelRate = int(input('\nEnter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): '))
   while fuelRate < 0 or fuelRate >9:
      print('ERROR: Fuel rate must be between 0 and 9, inclusive'+'\n')
      fuelRate = int(input('Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): '))
   if fuelRate > currentFuel:
      return currentFuel
   else:
      return fuelRate

def updateAcceleration(gravity, fuelRate):

    acceltp1 = (gravity)*(fuelRate/5-1)
    return acceltp1
	
def updateAltitude(altitude, velocity, acceleration):

      alt1 = altitude + velocity + (acceleration/2)
      if alt1 < 0:
         return 0
      else:   
         return alt1

def updateVelocity(velocity, acceleration):
   
   vel1 = velocity + acceleration
   return vel1

def updateFuel(fuel, fuelRate):
   
   fuel1 = fuel-fuelRate
   if fuel1 < 0:
      return 0
   else:
      return fuel1

def displayLMLandingStatus(velocity):
   
   if velocity <= 0 and velocity >= -1:
      print('\nStatus at landing - The eagle has landed!')
   if velocity < -1 and velocity > -10:
      print('\nStatus at landing - Enjoy your oxygen while it lasts!')
   if velocity <= -10:
      print('\nStatus at landing - Ouch - that hurt!')
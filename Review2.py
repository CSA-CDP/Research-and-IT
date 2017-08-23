#Collin Patterson
#8/26/2016
#Mr. Davis
#Advanced Computer Programming

class Car():
    def __init__(self, color, year, speed):
        print ('You have a ', color,' car from ', year,' that can go ', speed,' miles per hour.')

color = input('What color is your car? ')
year = input('What year is your car? ')
speed = input('What is the top speed of your car? ')
Car(color, year, speed)
#Wind Chill and Frostbite Calculator

#This program calculates the wind chill based on the air temperature and
#wind speed provided by a user. 

#Temperature is accepted in both Fahrenheit and Celsius, with
#wind speeds accepted in both MPH and KMPH. 

#Additionally, Frostbite is evaluated and provides the necessary information
#to the user based on the calculated wind chill.

#Conversion method for celsius to fahrenheit
def celsiusToFahrenheit(temp):
    return (temp * 1.8) + 32

#Conversion method for fahrenheit to celsius
def fahrenheitToCelsius(temp):
    return (temp - 32) / 1.8

#Conversion method for kmph to mph
def kmphToMPH(km):
    return km / 1.609

#Method to get the temperature unit entered by user
#Can be represented by Celsisus, C, Fahrenheit, or F
def getTemperatureUnit():
    #Use a loop to continuously ask for a temperature unit if a valid one is not entered
    while True:
        inputString = input("Enter a temperature unit (Celsius or Fahrenheit): ").lower() #Convert to lowercase for simplicity
        if inputString in ['c', 'celsius']:
            return 'C'
        elif inputString in ['f', 'fahrenheit']:
            return 'F'
        else:
            print("Invalid temperature unit.")

#Method to get the wind speed unit entered by user
#Can be represented by MPH or KMPH
def getWindSpeedUnit():
    #Use a loop to continuously ask for a wind speed unit if a valid one is not entered
    while True:
        inputString = input("Enter a wind speed unit (MPH or KMPH): ").lower() #Convert to lowercase for simplicity
        if inputString in ['mph', 'kmph']:
            return inputString
        else:
            print("Invalid wind speed unit.")

#Method to calculate the wind chill based on the entered values
def calculateWindChill(airTemperature, windSpeed):
    #Calculate wind chill only if air temperature < 50F and windspeed > 3MPH, otherwise wind chill set to air temperature
    if (airTemperature < 50 and windSpeed > 3):
        return 35.74 + 0.6215 * airTemperature - 35.75 * windSpeed ** 0.16 + 0.4275 * airTemperature * windSpeed ** 0.16
    else:
        return airTemperature #No wind chill

temperatureUnit = getTemperatureUnit()
temperatureValue = float(input("Enter a temperature value: "))

#If our temperature unit is entered in Celsius, convert to Fahrenheit
if (temperatureUnit == 'C'):
    temperatureValue = celsiusToFahrenheit(temperatureValue)

windSpeedUnit = getWindSpeedUnit()
windSpeedValue = float(input("Enter a wind speed: "))

#If our wind speed unit is entered in KMPH, convert to MPH
if (windSpeedUnit == "kmph"):
    windSpeedValue = kmphToMPH(windSpeedValue)

#If our wind speed value is negative, print and exit program
if (windSpeedValue < 0):
    print("Negative wind speed value not accepted.")
    exit()

windChillFahrenhiet = calculateWindChill(temperatureValue, windSpeedValue)
windChillCelsius = fahrenheitToCelsius(windChillFahrenhiet)

print("The wind chill is: %.2f" % (windChillFahrenhiet) + "ºF / %.2f" % (windChillCelsius) + "ºC")

frostbiteTime = ""
if (windChillFahrenhiet < -60):
    frostbiteTime = "5 minutes"
elif (windChillFahrenhiet < -35):
    frostbiteTime = "10 minutes"
elif (windChillFahrenhiet < -17):
    frostbiteTime = "30 minutes"
else:
    frostbiteTime = "unlikely"

print("The time to Frostbite is: " + frostbiteTime)
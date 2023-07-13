#Write a program to convert temperature from degree centigrade to fahrenheit by using function.
def centigrade_to_fahrenheit(p):
  F=(1.8*p)+32
  return F 
celsius = int(input("Enter  temperature in centigrade:"))
convert_temperature= centigrade_to_fahrenheit(celsius)
print("Temperature in degree fahrenheit:",convert_temperature)
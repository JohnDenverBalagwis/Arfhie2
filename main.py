# 1 celsius to farenheit
celsius = float(input('Input temperature in Centigrade: '))

fahrenheit = (celsius * 1.8) + 32

print('%0.3f degree Fahrenheit\n' % fahrenheit)


# 3 km to miles
kilometers = float(input("Input kilometers per hour: "))

conversion = 0.621371

miles = kilometers * conversion

print('%0.2f miles per hour\n' % miles)

# 4 waaah
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))

sum = (num1 + num2)
difference = (sum - num3)
product = (difference * num4)
quotient = (product / num5)

print(num1, "+", num2, "=", sum)
print(sum, "-", num3, "=", difference)
print(difference, "*", num4, "=", product)
print(quotient, "/", num5, "=", quotient)


# 5 Hour to min
hours = int(input("\nInput hours: "))
total = hours * 60
print("The number of minutes is: " + str(total) + " minutes")


# 6 Min to Hour
user_input = int(input("\nInput minutes: "))

minutes = user_input % 60
total = int(user_input / 60)

print("The number of hours is: " + str(total) + " hours, " + str(minutes) + " minutes")

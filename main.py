# Day 3 - Exercise - Odd or Even

#Module

#number = input("Write a number: ")

#module = int(number) % 2

#if module == 0:
  #print(f"The number {number} is even ")
#else:
  #print(f"The number {number} is odd ")

#IMC calc

weight = input("Write your weight: ")
height = input("Write your height: ")

calcIMC =  (float(weight) / float(height) ** 2) * 10000


print("Your IMC is: " + str(calcIMC))

#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.



if calcIMC < 18.5:
  print("You are underweight")
elif calcIMC >= 18.5 and calcIMC < 25:
  print("You have a normal weight")
elif calcIMC >= 25 and calcIMC < 30:
  print("You are slightly overweight")
elif calcIMC >= 30 and calcIMC < 35:
  print("You are obese")
else:
  print("You are clinically obese")
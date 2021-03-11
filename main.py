# Day 3 - Exercise - Odd or Even

#Module

number = input("Write a number: ")

module = int(number) % 2

if module == 0:
  print(f"The number {number} is even ")
else:
  print(f"The number {number} is odd ")
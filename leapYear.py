year = int(input("Write a year: "))

print(f"module 4: {year % 4}")
print(f"module 100: {year % 100}")
print(f"module 400: {year % 400}")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("This year is leap !!!")
    else:
      print("This year is not leap !!!")
  else:
    print("This year is leap !!!")  
else:
  print("This year is not leap !!!")

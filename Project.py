timetable = []
#monday
timetable.append(["JAVASCRIPT","UX RESEARCH","PYTHON"])
#tuesday
timetable.append(["NYJ","PROFESSIONL DEVELOPMENT","KOTLIN"])
#wednesday
timetable.append(["STARTUP 101","UX/UI DESIGN","IOT"])
#thursday
timetable.append(["PYTHON","SHOW & TELL","INDUSTRIAL DESIGN"])
#saturday
timetable.append(["PYTHON","UI/UX DEVELOPMENT","MAKE-UP"])

print(timetable)


day = input("Day of the week?")

lessons = []
if day == "Monday":
    print(timetable[0])
elif day == "Tuesday":
    print(timetable[1])
elif day == "Wednesday":
    print(timetable[2])
elif day == "Thursday":
    print(timetable[3])
else:
    print("Not a valid week day!")      


day = input("Day of the week?")
period = int(input("Lesson number (1 to 5):"))
while period<1 or period>5:
  period = int(input("Lesson number (1 to 5):"))
 
lesson=""
if day=="Monday":
  print(timetable[0][period-1])
elif day=="Tuesday":
  print(timetable[1][period-1])
elif day=="Wednesday":
  print(timetable[2][period-1])
elif day=="Thursday":
  print(timetable[3][period-1])
elif day=="Friday":
  print(timetable[4][period-1])
else:
  print("Not a valid week day!")


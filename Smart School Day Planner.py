print("=== smart school day planner ===")
print("answer 3 quick questions and i will plan your day!\n")
day=input("what day is it?(monday to sunday):").strip().capitalize()
weather=input("what is the weather?(sunny/rainy/cloudy):").strip().lower()
homework=input("is your homework done?(yes/no):").strip().lower()
print()
print(f"=== your plan for {day} ===")
print("-"*35)
if day in ("saturday", "sunday"):
    print("day type : weeknend - enjoy your free time!")
elif day =="monday":
    print("day type : first day of the week. pack your weekly planner.")
elif day == "friday":
    print("day type : last school day. return library books today.")
elif day in ("tuesday", "wednesday", "thursday","friday"):
    print("day type: regular school day. stay focused!")
else:
    print("day type: day not recognised. please check the spelling.")
if weather == "sunny" and homework == "yes":
    print("after school: head to the park - great weather and homework is done!")
if weather == "rainy" or weather == "cloudy":
    print("weather tip: pack your umbrella - it may get wet outside.")
if not (homework == "yes"):
    print("homework: not done yet. finish homework, then watch your favourite show.")
elif weather =="sunny" and homework == "yes" and not (day in ("saturday", "sunday")):
    print("best plan: all set for a great school day - you aree prepared!")
elif day in ("saturday", "sunday") and weather =="sunny":
    print("best plan: perfect weekend weather - head outside and have fun!")
else:
    print("best plan: take it one step at a time - you have got this!")
print()
print("plan complete! have a wonderful day!")
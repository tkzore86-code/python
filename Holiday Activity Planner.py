print("--------------------------------")
print("    welcome to holiday planner!    ")
print("================================")
print()

print("step1: pick your month")
print(" 1-december")
print(" 2-may")
print()

choice=int(input("enter 1 or 2: "))
print()
if choice == 1:
    print("step 2: pick your month type")
    print(" 1-christmas")
    print(" 2-summer vacation")
    print()

    holiday_type=int(input("enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("you picked: may")
        print("top days: a month")
        print("best for: after finals")
    else:
        print("you picked: may")
        print("top speed: on open day")
        print("best for: after may vacation")
elif choice == 2:
    print("step 2: picked your december type")
    print(" 1-christmas")
    print(" 2-picnic")
    print()

    car_type = int(input("enter 1 or 2: "))
    print()

    if car_type == 1:
        print("you picked: picnic")
        print("seats: 5 passengers")
        print("best for: family trips")
    else:
        print("you picked: christmas")
        print("seats: whole famaly")
        print("best for: family friends")

else:
    print("that was not a valid choice")
    print("please enter 1 for december or 2 may.")

print()
print("======================================")
print("      your custom holiday is ready!      ")
print("      enjoy the vacation!              ")
print("======================================")
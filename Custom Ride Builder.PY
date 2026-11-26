print("--------------------------------")
print("    welcome to ride builder!    ")
print("================================")
print()

print("step1: pick your vehicle")
print(" 1-bike")
print(" 2-car")
print()

choice=int(input("enter 1 or 2: "))
print()
if choice == 1:
    print("step 2: pick your bike type")
    print(" 1-scooty")
    print(" 2-mountain bike")
    print()

    bike_type=int(input("enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("you picked: scooty")
        print("top speed: 80 km/h")
        print("best for: city roads")
    else:
        print("you picked: mountain bike")
        print("top speed: 40 km/h")
        print("best for: off-road trails")
elif choice == 2:
    print("step 2: picked your car type")
    print(" 1-sedan")
    print(" 2-suv")
    print()

    car_type = int(input("enter 1 or 2: "))
    print()

    if car_type == 1:
        print("you picked: sedan")
        print("seats: 5 passengers")
        print("best for: family trips")
    else:
        print("you picked: suv")
        print("seats: 7 passengers")
        print("best for: off-road adventures")

else:
    print("that was not a valid choice")
    print("please enter 1 for bike or 2 cars.")

print()
print("======================================")
print("      your custom ride is ready!      ")
print("      enjoy the journey!              ")
print("======================================")
base=int(input("enter the number: "))
power=int(input("enter the power: "))

result=1

for i in range(power):
    result=result * base

print("result =", result)

Enter the number:2
Enter the power:3
result=8
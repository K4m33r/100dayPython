total_bill = float(input("Enter the total bill: "))
people_co = float(input("Enter the people number: "))
percent = float(input("Enter the tip percent '10, 12, 15': "))
each_person = total_bill * (1 + percent / 100)
final = each_person / people_co
print(f"Each person should pay: {round(final, 2)}")
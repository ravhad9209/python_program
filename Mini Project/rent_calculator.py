### Rent Calculator

## Inputs we need from the user
# Total rent
# chai_poha 
# electricity unit spend
# charge per Unit 
# persons living in room/flat 

## output
# Total amount you've to pay is

day = float(input("Enter the days = "))
total_rent = float(input("Enter total rent = "))
chai = float(input("Enter chai amount = "))
poha = float(input("Enter poha amount = "))
electricity_unit_spend = float(input("Enter elctricity unit = "))
charge_per_unit = float(input("Enter charge per Unit amount = "))
persons_living_in_room = float(input("enter the persons = "))

total_bill = electricity_unit_spend * charge_per_unit
total_chai = chai*day
total_poha_amount = poha*day

total_amount = ((total_rent+total_chai+total_poha_amount+total_bill)/persons_living_in_room)

print("Total amount you've to pay is : ", total_amount)
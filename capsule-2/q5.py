roses = int(input("Enter the number of roses: "))
#Assuming distance is in integer km
distance = int(input("Enter the distance in km: "))
if distance <= 5:
    delivery_charge = 25
elif distance <= 10:
    delivery_charge = 50
else:
    delivery_charge = 75
total_cost = (roses * 10) + delivery_charge
print(f"The total cost of delivery is: {total_cost}")
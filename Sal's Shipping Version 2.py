weight = int(input("How much does your package weigh? "))
premium = 105.00
# Ground Shipping
if weight <= 2:
  GroundShipping = (weight * 1.50) + 20.00
elif weight > 2 and weight <= 6:
  GroundShipping = (weight * 3.00) + 20.00
elif weight > 6 and weight <= 10:
  GroundShipping = (weight * 4.00) + 20.00
else:
  GroundShipping = (weight * 4.75) + 20.00
print("Groud Shipping is: $", GroundShipping)

# Premium Shipping
print("Premium Shipping is: $", GroundShipping + premium)

# "Drone Shipping"

if weight <= 2:
  DroneShipping = weight * 4.50
elif weight > 2 and weight <= 6:
  DroneShipping = weight * 9.00
elif weight > 6 and weight <= 10:
  DroneShipping = weight * 12.00
else:
  DroneShipping = weight * 14.25
print("Drone Shipping is: $", DroneShipping)

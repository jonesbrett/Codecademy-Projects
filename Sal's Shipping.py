weight = 41.5
premium = 105.00
# Ground Shipping
if weight <= 2:
  print("Ground Shipping = ", (weight * 1.50) + 20.00)
elif weight > 2 and weight <= 6:
  print("Ground Shipping = ", (weight * 3.00) + 20.00)
elif weight > 6 and weight <= 10:
  print("Ground Shipping = ", (weight * 4.00) + 20.00)
else:
  print("Ground Shipping = ", (weight * 4.75) + 20.00)

# Premium Shipping
print("Premium shipping = Ground Shipping +", premium)

# "Drone Shipping"

if weight <= 2:
  print("Drone Shipping = ", weight * 4.50)
elif weight > 2 and weight <= 6:
  print("Drone Shipping = ", weight * 9.00)
elif weight > 6 and weight <= 10:
  print("Drone Shipping = ", weight * 12.00)
else:
  print("Drone Shipping = ", weight * 14.25)

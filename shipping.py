weight = 4.8

# Ground Shipping

if weight <= 2:
  cost_ground = weight * 1.5 + 20
  print("Ground Shipping $", cost_ground)
elif weight <= 6:
  cost_ground = weight * 3.0 + 20
  print("Ground Shipping $", cost_ground)
elif weight <= 10:
  cost_ground = weight * 4.0 + 20
  print("Ground Shipping $", cost_ground)
elif weight > 10:
  cost_ground = weight * 4.75 + 20
  print("Ground Shipping $", cost_ground)
else:
  print("Erro")

cost_ground_premium = 125.00
print("Ground Shipping Premium $", cost_ground_premium)

# Drone Shipping

if weight <= 2:
  cost_ground = weight * 4.50
  print("Drone Shipping $", cost_ground)
elif weight <= 6:
  cost_ground = weight * 9.00
  print("Drone Shipping $", cost_ground)
elif weight <= 10:
  cost_ground = weight * 12.00
  print("Drone Shipping $", cost_ground)
elif weight > 10:
  cost_ground = weight * 14.25
  print("Drone Shipping $", cost_ground)
else:
  print("Erro")
weight = 0

##Ground Shipping
if weight <= 2:
  ground_shipping = weight * 1.50 + 20
elif weight <= 6:
  ground_shipping = weight * 3.00 + 20
elif weight <= 10:
  ground_shipping = weight * 4.00 + 20
else:
  ground_shipping = weight * 4.75 + 20
print("Ground shipping cost: $", ground_shipping)

##Premium shipping 
premium_shipping = 125.00
print("Premium shipping cost: $", premium_shipping)

##Drone shipping 
if weight <= 2:
  drone_shipping = weight * 4.50
elif weight <= 6:
  drone_shipping = weight * 9.00
elif weight <= 10:
  drone_shipping = weight * 12
else:
  drone_shipping = weight * 14.25
print("Drone shipping cost: $", drone_shipping)




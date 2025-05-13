from django.db import models

# Cart - This model keeps track of the items a user adds 
# to their shopping cart before they decide to buy them. 
# It's like a shopping basket in a store.



# CartItem - This model stores the individual items in a cart. 
# It records which product the user added to their cart and 
# how many of that item they want to buy.



# Order - This model represents a completed purchase. Once a user 
# checks out and buys products, an order is created to keep track 
# of everything they bought and the total price.



# OrderItem - This model stores each individual product in an order. 
# For example, if a user buys 2 T-shirts, this model will store 2 items 
# in the order: one for each T-shirt.



# Payment - This model tracks how a user paid for their order. 
# It keeps details like the payment method (credit card, PayPal) 
# and how much money was paid.



# Coupon - : This model stores information about discount codes that users 
# can apply during checkout to get a reduction in the total price of their order. 
# For example, a user could enter a code like "SAVE20" to get 20% off their purchase. 
# The model keeps track of details such as the code, discount value, and 
# validity period (start and end date). It helps apply discounts during the 
# checkout process and makes the shopping experience more exciting for users.



# ReturnRequest - This model stores requests from users to return products 
# they’ve purchased. Sometimes users might want to return an item because 
# it doesn’t fit, or they changed their mind. This model keeps track of the 
# order the item came from, the product being returned, 
# the reason for the return (e.g., damaged, wrong size), and the status of the 
# return request (approved, rejected, pending). It helps manage the process of 
# returns and refunds in your store.



# Payment - This model tracks payments for orders. It stores details like 
# payment status (completed, pending, failed), the payment method (credit card, 
# PayPal, etc.), and the payment amount. When a user completes a purchase, 
# this model is updated with information about how they paid, and whether 
# the payment was successfully processed. This helps you keep track of the 
# financial side of each order and verify that payments are completed.



# Inventory Management - Inventory management is keeping track of how many 
# products you have in your store, like counting toys, so you know when to 
# restock and never sell something that's out of stock. It helps you manage 
# the number of items left, update it when something is sold, and 
# make sure customers can only buy what’s available.



# ShippingAddress - A ShippingAddress model stores the address where a 
# customer wants their order to be delivered. It typically includes fields like 
# the recipient's name, street address, city, postal code, and country. 
# This information is used to ensure the products are sent to the right location. 
# It also helps in calculating shipping costs and tracking the delivery process.




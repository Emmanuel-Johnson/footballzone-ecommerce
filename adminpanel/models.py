from django.db import models

# CategoryOffer - This is a more specific type of Offer model that is focused on 
# discounts or promotions applied to a whole category of products. 
# For example, you might offer 10% off all Shoes or T-shirts. This model would 
# allow you to set offers for entire categories of products rather than 
# just individual items.



# ProductOffer - Similar to CategoryOffer, this model focuses on offers or discounts 
# applied to individual products. For example, you might have a specific product 
# like a T-shirt that is discounted by 15%. This model would store the details 
# of offers that are applied to specific products.



# SalesReport - This model helps you generate reports of sales performance over
# a given time period. It can store summary data like total sales (revenue), 
# the number of orders placed, and product quantities sold. This model is optional, 
# as you might want to generate these reports dynamically using data already stored 
# in your system. However, having this model can be helpful for tracking and 
# analyzing your store’s performance over time.



from django.db import models

# Category - This model groups products into categories. For example, 
# you could have categories like "T-shirts," "Shoes," or "Accessories." 
# It helps you organize your products.


# Product - This model stores the details of the things you're selling
# on your website. It contains information like the product’s name, price, 
# description, and an image of the product.



# ProductImage - This model stores extra images of the product. For example, 
# you might have a main image of a T-shirt, but you can also add images 
# showing the shirt from different angles or in different colors.



# ProductVariant - This model handles different versions of a product. 
# For example, if you sell T-shirts, the variant might be the size (S, M, L) 
# or color (Red, Blue, Green).



# Stock - This model tracks the quantity of each product variant (like size or color) 
# that is available in your inventory. For example, if you sell a T-shirt in sizes 
# Small, Medium, and Large, this model will store how many of each size is available 
# for purchase. It helps you keep track of how much stock you have left for each 
# product variant and ensures that users can only order items that are in stock.



# Wishlist - To let users save products they like but don’t want to buy right now.
# It helps them easily find those products later without searching again.



# ProductReview - To let customers share their opinions about the products they bought.
# Reviews help build trust and guide other users in making buying decisions.


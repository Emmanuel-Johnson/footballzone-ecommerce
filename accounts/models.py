from django.db import models

# User - This model represents the people who will use your website 
# like customers or admins. It stores their basic details such as 
# name, email, password, and whether they are active or not.)


# UserProfile - This model is like a personal profile page for each user. 
# It stores extra information about users, such as their phone number 
# and profile picture.


# Address - This model keeps track of where the user lives or
# where they want their products to be shipped. It stores details like 
# their address, city, state, and zip code.



# Wallet - This model keeps track of the virtual wallet for each user. 
# It stores the user's balance of credits or refunds that they can use 
# to buy products or services on your website. This balance can be updated
# when the user gets a refund, a credit from returns



# Referral - This model helps track referral programs. When a user shares 
# their unique referral code with a friend, this model keeps track of 
# who referred whom, and it records the rewards earned by both the referrer 
# (the person who shared the code) and the referee (the person who used the code). 
# It helps encourage users to invite others and rewards them with bonuses like 
# discounts or credits.



# OTPVerification - This model helps with verifying a user’s identity using an 
# OTP (One-Time Password). For example, when a user signs up, logs in, resets their 
# password, or does anything sensitive, they get a short code (like "123456") on 
# their phone or email. This model stores that code and keeps track of when it was 
# sent and whether it was used or expired.




restart for daily mininum 30 min
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)



class Account(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager() 

    def __str__(self):
        return self.email



class Address(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='addresses')

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    alt_phone = models.CharField(max_length=10, blank=True, null=True)

    pincode = models.CharField(max_length=6)
    locality = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    landmark = models.CharField(max_length=100, blank=True, null=True)

    ADDRESS_CHOICES = [
        ('home', 'Home'),
        ('work', 'Work'),
    ]
    address_type = models.CharField(max_length=10, choices=ADDRESS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_default = models.BooleanField(default=False)  # optional

    def __str__(self):
        return f"{self.name} - {self.locality}, {self.city}"



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





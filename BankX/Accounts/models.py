from django.db import models
from django.contrib.auth.models import User  # Import Django's built-in User model


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link the account to a user
    account_number = models.CharField(max_length=10, unique=True)
    initial_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_type = models.CharField(max_length=20, choices=[
        ('Savings', 'Savings'),
        ('Current', 'Current'),
        ('Student', 'Student'),
    ])
    account_pin = models.PositiveIntegerField()

    def __str__(self):
        return self.account_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.save()

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.save()

    def get_balance(self, in_string=False):
        if in_string:
            return f"Your Account Balance is: {self.account_balance}"
        else:
            return self.account_balance
        
    def get_account_type(self):
        return self.account_type

    def __str__(self):
        return f"Account {self.account_no} for {self.account_owner.name}"

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class User(models.Model):
#     # Add your custom fields here.
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     age = models.PositiveIntegerField()
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255,default='password')

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
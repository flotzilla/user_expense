from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("Food", "Food"),
        ("Travel", "Travel"),
        ("Utilities", "Utilities"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
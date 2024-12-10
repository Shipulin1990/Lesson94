from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Categories(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField()
    category = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.product_id

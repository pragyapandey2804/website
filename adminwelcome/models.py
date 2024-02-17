from django.db import models

class User(models.Model):
    tenement_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'  # Ensure the table name matches the actual table name in the database


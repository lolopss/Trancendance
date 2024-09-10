from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    nickname = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        # Hash the raw password and store it.
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        # Check if the provided raw password matches the hashed password.
        return check_password(raw_password, self.password)
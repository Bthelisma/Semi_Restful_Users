# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 5:
            errors["first_name"] = "First_name should be more than 5 characters"
        if len(postData['first_name']) < 5:
            errors["last_name"] = "Last_name should be more than 5 characters"
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be blank"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __str__(self):
            return "<User object: {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.created_at)

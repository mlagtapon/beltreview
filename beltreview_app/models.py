from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] =  "Invalid email address"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if len(postData['confirm']) != len(postData['password']):
            errors["confirm"] = "Password does not match"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email."
        return errors

    def login_validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email_login']):
            errors['login'] = "Invalid Email/Password."
        if len(postData['password_login']) < 8:
            errors['login'] = "Invalid Email/Password."
        return errors
        
class BookManager(models.Manager):
    def book_validator(self, postData):
        errors={}
        if len(postData['title']) == 0:
            errors['title'] = "Title is required."
        if len(postData['reviews']) < 5:
            errors['reviews'] = "Description must be at least 5 characters."
        if len(postData['ratings']) == 0 :
            errors['ratings'] = "Ratings must be between 0 and 5"
        return errors
        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    def __repr__(self): 
        return f"<{self.id} {self.first_name} {self.last_name} {self.email} {self.password} {self.created_at} {self.updated_at} "

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    reviews = models.TextField(max_length=255)
    ratings = models.ManyToManyField(User, related_name="rated_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BookManager()
    def __repr__(self): 
        return f"<{self.id} {self.title} {self.author} {self.reviews} {self.ratings} {self.created_at} {self.updated_at} "
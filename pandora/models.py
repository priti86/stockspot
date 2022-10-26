from django.db import models

class Company(models.Model):
    index = models.IntegerField(primary_key=True, unique=True, null=False)
    company = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.company

class Friend(models.Model):
    name = models.CharField(max_length=100, null=False)
    index = models.IntegerField()

    def __str__(self):
        return self.name

class FavoriteFood(models.Model):
    index = models.IntegerField()
    foodlist = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.foodlist

class FavoriteFoodPeople(models.Model):
    index = models.IntegerField()
    foodlist = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.foodlist

class People(models.Model):
    registered = models.DateTimeField(null=True)
    index = models.IntegerField(null=True)
    company_id = models.ForeignKey(Company, to_field="index", on_delete=models.CASCADE,null=True)
    friends = models.ManyToManyField(Friend)
    favoriteFood = models.ManyToManyField(FavoriteFoodPeople)
    has_died = models.BooleanField(default=False)
    balance = models.CharField(max_length=100)
    eyeColor = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100)
    address = models.TextField(null=True)
    about = models.TextField(null=True)
    greeting = models.CharField(max_length=100)

    def __str__(self):
        return self.name

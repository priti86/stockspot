import json
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')
django.setup()

from pandora.models import People, Company, Friend, FavoriteFoodPeople

f = open('<file path from where data is expected to be loaded>', 'r')
obj = json.load(f)

for o in obj:
    newPeople = People(index=o["index"],
                       name=o["name"],
                       registered=o["registered"],
                       company_id = Company.objects.get(index=o["company_id"]),
                       has_died=o["has_died"],
                       eyeColor=o["eyeColor"],
                       balance=o["balance"],
                       gender=o["gender"],
                       email=o["email"],
                       phone=o["phone"],
                       address=o["address"],
                       about=o["about"],
                       greeting=o["greeting"],
                    )
    newPeople.save()
    for each_friend in o["friends"]:
        newPeople.friends.add(Friend.objects.get(index=each_friend.get("index")))
    for each_fruit in o["favouriteFood"]:
        newPeople.favoriteFood.add(FavoriteFoodPeople.objects.get(foodlist=each_fruit))
    newPeople.save()
print("Load Data Done")

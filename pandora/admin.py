from django.contrib import admin
from .models import FavoriteFood, Company, Friend, FavoriteFoodPeople, People
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CompanyResource(resources.ModelResource):
   class Meta:
      model = Company
      import_id_fields = ['index']

class CompanyAdmin(ImportExportModelAdmin):
   resource_class = CompanyResource

class FavoriteFoodPeopleResource(resources.ModelResource):
    class Meta:
        model = FavoriteFoodPeople
        fields=["index","favoriteFood"]

class FavoriteFoodPeopleAdmin(ImportExportModelAdmin):
    resource_class = FavoriteFoodPeopleResource

class FriendResource(resources.ModelResource):
    class Meta:
        model = Friend
        fields=["index","name"]

class FriendAdmin(ImportExportModelAdmin):
    resource_class = FriendResource

class PeopleResource(resources.ModelResource):
   class Meta:
       model = People
       import_id_fields = ["index"]
       widgets = {"friends":{"field":"index"},"favoriteFood":{"field":"index"}}

class PeopleAdmin(ImportExportModelAdmin):
   resource_class = PeopleResource


admin.site.register(FavoriteFoodPeople)
admin.site.register(Company,CompanyAdmin)
admin.site.register(People,PeopleAdmin)
admin.site.register(FavoriteFood)
admin.site.register(Friend)



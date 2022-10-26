import json
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from .models import People, Company

FRUITS = ["orange", "apple", "banana", "strawberry"]
VEGETABLES = ["beetroot", "celery", "carrot"]
GENERIC_ERROR = "ops!!! Something went wrong."


def index(request):
    return render(request, r"/Users/pritisharma/PycharmProjects/djangoProject1/pandora/templates/index.html")


def get_all_employees_of_company(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        if company_name:
            company_id = Company.objects.filter(company=company_name).values("index")
            if company_id:
                peoples = People.objects.filter(company_id=company_id[0]["index"])
                context = {
                    'peoples': peoples
                }
            else:
                return HttpResponse("Company Name not found in database.Please enter a valid name")
        return render(request,
                      r"/Users/pritisharma/PycharmProjects/djangoProject1/pandora/templates/view_employees_of_a_company.html",
                      context)
    elif request.method == 'GET':
        return render(request,
                      r"/Users/pritisharma/PycharmProjects/djangoProject1/pandora/templates/get_employees_of_a_company.html")
    else:
        return HttpResponse(GENERIC_ERROR)


def get_employee_info(request):
    if request.method == 'POST':
        response = {}
        people_name = request.POST['name']
        if people_name:
            people = pd.DataFrame.from_records(
                People.objects.filter(name=people_name).values("name", "age", "favoriteFood__foodlist"))
            if not people.empty:
                age = people["age"].to_list()[0]
                food = people["favoriteFood__foodlist"].to_list()
                fruits = [x for x in food if x in FRUITS]
                vegetables = [x for x in food if x in VEGETABLES]
                response["name"] = people_name
                response["age"] = age
                response["fruits"] = fruits
                response["vegetables"] = vegetables

                return render(request,
                              r"/Users/pritisharma/PycharmProjects/djangoProject1/pandora/templates/view_employee_details.html",
                              response)
            else:
                return HttpResponse("This employee was not found in our database.")
    elif request.method == 'GET':
        return render(request,
                      r"/Users/pritisharma/PycharmProjects/djangoProject1/pandora/templates/get_employee_info.html")
    else:
        return HttpResponse(GENERIC_ERROR)


def get_common_details_between_employees(request):
    if request.method == 'POST':
        response = {}
        people_name1 = request.POST["name1"]
        people_name2 = request.POST["name2"]
        my_input = [people_name1, people_name2]
        if people_name1 and people_name2:
            people_df = pd.DataFrame.from_records(
                People.objects.filter(name__in=my_input).values("name", "age", "address", "phone", "eyeColor",
                                                                "has_died", "friends__index"))
            if not people_df.empty:
                temp_people_df = people_df[["name", "age", "address", "phone"]]
                temp_people_df.drop_duplicates(inplace=True)
                friends_list = people_df["friends__index"].to_list()
                seen = set()
                response["friends_in_common"] = [x for x in friends_list if x in seen or seen.add(x)]
                response["still_alive"] = list(set(people_df[people_df["has_died"] == False]["name"].to_list()))
                response["brown_eyeColor"] = list(set(people_df[people_df["eyeColor"] == 'brown']["name"].to_list()))
                response["employee_details"] = temp_people_df.to_dict(orient='records')
                return HttpResponse(json.dumps(response))
            else:
                return HttpResponse("Looks like values entered were not correct. Please re-enter.")
    elif request.method == 'GET':
         return render(request,
                  r"/Users/pritisharma/PycharmProjects/djangoProject1/pandora/templates/get_common_details_of_employees.html")
    else:
        return HttpResponse(GENERIC_ERROR)
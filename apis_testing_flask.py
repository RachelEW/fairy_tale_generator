# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:38:29 2019

@author: winkl
"""
import requests
import random
import config
import app


def choose_extra_value():
    possible_parameters = ["otherInsult", "otherCatchPhrase", "otherBuzzword", "stringShort", "stringWords", "otherInsult"]
    for i in range(1):
       num = random.randint(0,5)
       print(num)
    extraValue = possible_parameters[num]
    print(extraValue)
    return extraValue

def generate_user(extraValue):
    endpoint = "https://app.fakejson.com/q"
    payload = {
        "token": config.api_key,
        "data": {
          "first_name": "nameFirst",
          "last_name": "nameLast",
          "namePrefix": "namePrefix",
          "numberInt": "numberInt",
          "numberInt|x,y": "numberInt|1,10",
          "personLanguage": "personLanguage",
          "personSkill": "personSkill",
          "personTitle": "personTitle",
          "personDegree": "personDegree",
          extraValue: extraValue,
          "location": {
                  "city": "addressCity",
                  "country": "addressCountry"
                  },
          "_repeat": 1
        }
    };
    response = requests.post(endpoint, json = payload)
    protagonist = response.json()
    print(protagonist)
    return protagonist

def define_protagonist():
    extraValue = choose_extra_value()
    protagonist = generate_user(extraValue)
    return protagonist

def no_of_pets(protagonist):
    smallInt = protagonist['numberInt|x,y']
    return smallInt

def first_name(protagonist):
    fName = protagonist['first_name']
    return fName

def last_name(protagonist):
    lName = protagonist['last_name']
    return lName

def city(protagonist):
    city = protagonist ['location']['city']
    return city

def job_title(protagonist):
    job_title = protagonist['personTitle']
    return job_title

def generate_advice():
    for i in range(1):
       slip_no = str(random.randint(1,220))
    endpoint_advice = "https://api.adviceslip.com/advice/"
    response = requests.get(endpoint_advice + slip_no)
    advice_slip = response.json()
    advice = advice_slip["slip"]["advice"]
    print(advice)
    return advice

def generate_pet(user_animal):
    pet = user_animal
    print(pet)
    return pet

def choose_visitor(user_number):
    user_number = int(user_number)
    while user_number > 6:
        user_number = user_number % 2
    if user_number ==1:
        visitor = "wizard"
    elif user_number ==2:
        visitor = "dragon"
    elif user_number ==3:
        visitor = "mysterious floating figure clothed in black"
    elif user_number ==4:
        visitor = "witch"
    elif user_number ==5:
        visitor = "unicorn"
    elif user_number ==6:
        visitor = "elf"
        print(visitor)
    return visitor

#Other values for FakeJSON:
#          "companyName": "companyName",
#          "companyDepartment": "companyDepartment",
#          "companyIndustry": "companyIndustry",
#                    "name": "name",
#                              "job": {
#                  "company": "companyName",
#                  "position": "personTitle"
#                  },

##############
"""TESTING"""
##############


# extraValue = choose_extra_value()
# protagonist = generate_user(extraValue)
# advice = generate_advice()
# smallInt = no_of_pets(protagonist)
# fName = first_name(protagonist)
# lName = last_name(protagonist)
# city = city(protagonist)
# job_title = job_title(protagonist)
# pet = generate_pet(animal)
# visitor = choose_vistor(user_number)

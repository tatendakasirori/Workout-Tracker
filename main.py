import requests
import os 
from dotenv import load_dotenv
from datetime import datetime

############ USING THE NUTRITIONIX API ##############
load_dotenv()
NU_APP_ID = os.getenv("NU_APP_ID") 
NU_API_KEY = os.getenv("NU_API_KEY")
WEIGHT = os.getenv("WEIGHT")
HEIGHT = os.getenv("HEIGHT")
AGE = os.getenv("AGE")

nu_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

query = input("Describe your excercise:\n")

nu_parameters={
    'query': query,
    'weight_kg':WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE    
}

nu_headers={
    'Content-Type': 'application/json',
    "x-app-id":NU_APP_ID,
    "x-app-key":NU_API_KEY,
}

nu_response = requests.post(url=nu_url, json=nu_parameters, headers=nu_headers)

print(nu_response.status_code)
nu_result = nu_response.json()
print(nu_result)
#get a list of exercises with their ducation and calories 
nu_list = [ {
    'exercise':exercise_dict['name'].capitalize(),
    'duration':exercise_dict['duration_min'],
    'calories':exercise_dict['nf_calories']
}
           for exercise_dict in nu_result["exercises"]]


# ############# GETTING FORMATTED TIME AND DATE #########

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime('%H:%M:%S')

# ############ USING THE SHEETY API ###########

SH_URL = os.getenv('SH_URL')

for ex in nu_list: # looping over exercises in nu_list and entering them one at a time 
    sh_parameters = {
        'workout':{
            'date': date,
            "time": time,
            "exercise": ex['exercise'],
            "duration": ex['duration'],
            "calories": ex['calories']
        }
    }

    sh_headers={
        'Authorization': os.getenv("AUTHORIZATION"),
        "Content-Type": "application/json"
        }

    sh_response = requests.post(url=SH_URL, json=sh_parameters, headers=sh_headers)
    print(sh_response.status_code)
    print(sh_response.json())
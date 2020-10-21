import requests
import json


def get_categories_list(url):
    response_categories = requests.get(url)
    jsonn_response_categories = response_categories.json()

    temp_lst = []

    for a in jsonn_response_categories["trivia_categories"]:
        temp_lst.append(a["name"])

    return temp_lst


def get_session_token():
    token_raw = requests.get("https://opentdb.com/api_token.php?command=request")
    token = token_raw.json()

    code = token["token"]

    return code


def get_categories_dict():
    resp = requests.get("https://opentdb.com/api_category.php")
    response = resp.json()

    return respone

def get_questions(token, category_id, difficulty):
    questions_lst = []  
    response = requests.get(f"https://opentdb.com/api.php?amount=10&category={category_id}&token={token}")

    for num in response["results"]:
        if num["difficulty"] == difficulty:
            questions_lst.append(num["question"])
        else:
            continue

    

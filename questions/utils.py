import requests
import json
import base64
import re


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

    return response

def get_question_answers_dct(token, category_id, difficulty):
    response = requests.get(f"https://opentdb.com/api.php?amount=10&category={category_id}&token={token}&difficulty={difficulty}&encode=urlLegacy")
    resp = response.json()

    print(resp)
    print(resp["results"][0]["question"])
    print(type(resp["results"][0]["question"]))

    ## decode QUESTIONS

    
    for num in range(len(resp["results"])):

        question = resp["results"][num]["question"]


        new = question.replace('%2C',',').replace('+',' ').replace('%3F','?').replace('%22','"').replace('%27',"'").replace('%E2%80%99',"'").replace("%C5%91", "ő").replace('%','$').split()
        result_str = ''

        for a in new:
            result_str += a
            result_str += " "


        resp["results"][num]["question"] = result_str

    ## decode QUESTIONS


    ## decode ANSWERS

    for num in range(len(resp["results"])):

        correct_answer = resp["results"][num]["correct_answer"]  # string
        incorrect_answers = resp["results"][num]["incorrect_answers"] # list

    ###################################################################################
        new = correct_answer.replace('%2C',',').replace('+',' ').replace('%3F','?').replace('%22','"').replace('%27',"'").replace('%E2%80%99',"'").replace('%','$').replace("%C5%91", "ő").split()

        result_str = ''

        for a in new:
            result_str += a
            result_str += " "

        new_correct_answer = result_str
        resp["results"][num]["correct_answer"] = new_correct_answer

    #########################################################################

        new_incorrect_answers = []

        for a in range(len(incorrect_answers)):
            new = incorrect_answers[a].replace('%2C',',').replace('+',' ').replace('%3F','?').replace('%22','"').replace('%27',"'").replace('%E2%80%99',"'").replace('%','$').replace("%C5%91", "ő").split()

            result_str = ''

            for a in new:
                result_str += a
                result_str += " "

            new_incorrect_answers.append(result_str)

        resp["results"][num]["incorrect_answers"] = new_incorrect_answers
        

    ## decode ANSWERS





    dct = {}
    

    for a in resp["results"]:
        dct[a["question"]] = []
        dct[a["question"]].append(a["correct_answer"])
        dct[a["question"]] += a["incorrect_answers"]


    return dct



    


    

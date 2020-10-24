from django.shortcuts import render
import requests
import json
import random
from questions import utils

    #if ["questions", "type", "score"] not in request.session:
    #    request.session["questions"] = []
    #    request.session["type"] = []
    #    request.session["score"] = []
    #else:
    #    pass
# Create your views here.




def home_page(request):

    request.session["q_index"] = 0
    request.session["category"] = ""
    print(request.session["q_index"])

    request.session["token"] = utils.get_session_token()

    return render(request, 'questions/home5.html')



def quiz(request):

    if request.method == "GET":      
        request.session["score"] = 0
        request.session["chosen_category_id"] = "0"

        
        request.session["category_name_list"] = []

        categories = utils.get_categories_dict()
        for num in categories["trivia_categories"]:
            request.session["category_name_list"].append(num["name"])
            


        return render(request, "questions/quiz_home.html", {
            "list": request.session["category_name_list"]
        })


    else:

        request.session["category"] = request.POST["category"]
        request.session["difficulty"] = request.POST["difficulty"]


        categories = utils.get_categories_dict()
        chosen_category_id = []

        for num in categories["trivia_categories"]:
            if num["name"] == request.session["category"]:
                chosen_category_id.append(num["id"])
            else:
                continue

        request.session["chosen_category_id"] = chosen_category_id[0]
        print("category id is:" + f'{request.session["chosen_category_id"]}')


        question_answers_dct = utils.get_question_answers_dct(request.session["token"], str(request.session["chosen_category_id"]), request.session["difficulty"])
        request.session["question_answers_dct"] = question_answers_dct

        print(request.session["question_answers_dct"])



        if len(list(request.session["question_answers_dct"].values())[request.session["q_index"]]) == 2:

            return render(request, "questions/test2.html", {
                "question": list(request.session["question_answers_dct"].keys())[request.session["q_index"]]  
            })

        else:

            while True:

                opt = []

                option1 = list(request.session["question_answers_dct"].values())[request.session["q_index"]][random.randint(0, 3)]
                opt.append(option1)

                option2 = list(request.session["question_answers_dct"].values())[request.session["q_index"]][random.randint(0, 3)]
                opt.append(option2)

                option3 = list(request.session["question_answers_dct"].values())[request.session["q_index"]][random.randint(0, 3)]
                opt.append(option3)

                option4 = list(request.session["question_answers_dct"].values())[request.session["q_index"]][random.randint(0, 3)]
                opt.append(option4)

                if len(opt) == len(set(opt)):
                    break
                else:
                    continue


            return render(request, "questions/test.html", {
                "question": list(request.session["question_answers_dct"].keys())[request.session["q_index"]],
                "option1": opt[0],
                "option2": opt[1],
                "option3": opt[2],
                "option4": opt[3],              
            })





def next_question(request):
    try:
        if request.method == "POST":     
            correct = list(request.session["question_answers_dct"].values())[request.session["q_index"]][0]

            if "bool" in list(request.POST.keys()):
                if request.POST["bool"] == correct:
                    request.session["score"] += 1
                else:
                    pass 
            
            else:
                if request.POST["opt"] == correct:
                    request.session["score"] += 1
                else:
                    pass

            print(request.session["score"])


            request.session["q_index"] += 1

            if len(list(request.session["question_answers_dct"].values())[request.session["q_index"]]) == 2:

                return render(request, "questions/test2.html", {
                    "question": list(request.session["question_answers_dct"].keys())[request.session["q_index"]]  
                })

            else:

                while True:

                    opt = []

                    option1 = list(request.session["question_answers_dct"].values())[request.session["q_index"]][random.randint(0, 3)]
                    opt.append(option1)

                    option2 = list(request.session["question_answers_dct"].values())[request.session["q_index"]][random.randint(0, 3)]
                    opt.append(option2)

                    option3 = list(request.session["question_answers_dct"].values())[request.session["q_index"]][random.randint(0, 3)]
                    opt.append(option3)

                    option4 = list(request.session["question_answers_dct"].values())[request.session["q_index"]][random.randint(0, 3)]
                    opt.append(option4)

                    if len(opt) == len(set(opt)):
                        break
                    else:
                        continue

                print(opt)


                return render(request, "questions/test.html", {
                    "question": list(request.session["question_answers_dct"].keys())[request.session["q_index"]],                
                    "option1": opt[0],
                    "option2": opt[1],
                    "option3": opt[2],
                    "option4": opt[3],         
                })

    except:

        return render(request, "questions/score.html", {
            "score": request.session["score"]
        })







    

from django.shortcuts import render
from questions import utils

# Create your views here.

def index(request):
    return render(request, 'questions/index.html', {
        "list": utils.get_categories_list('https://opentdb.com/api_category.php')
    })


def quiz(request):

    if request.method == "POST":
        category = request.POST["category"]
        difficulty = request.POST["difficulty"]
        
        dict1 = utils.get_categories_dict()
        category_id = []

        for num in dict1["trivia_categories"]:
            if num["name"] == category:
                category_id.append(num["id"])
            else:
                continue

        token = get_session_token()



    
    return render(request, 'questions/quiz.html', {
        "question": questions_lst
    })
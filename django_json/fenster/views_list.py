from django.shortcuts import render

import random

def create_example():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return str(a) + " + " + str(b), a + b
    

def index(request):
    context = {
        "examples_math": [
            create_example(),
            create_example(),
            create_example()
        ],
        "i_am_teacher": True   
    }
    return render(
        request,               # Запрос
	    'fenster/index.html',  # путь к шаблону
        context                # подстановки
    )

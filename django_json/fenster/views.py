from django.shortcuts import render
from django.http import HttpResponse

import random
import json

def create_example():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return str(a) + " + " + str(b), a + b
    

def index(request):
    if request.method == 'POST':
        for elem in request.POST:
            print(elem, request.POST)
#        print(json.loads(request.body))
        body_unicode = request.body.decode('utf-8')
#        print(body_unicode)
        body_data = json.loads(body_unicode)
        print(body_data)
        return HttpResponse("<h1>Prosto text</h1>")
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

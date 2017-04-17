from django.shortcuts import render, redirect, HttpResponse
import datetime, time
import random
from random_words import RandomWords

def index(request):
    context = {

    "content":datetime.datetime.now().strftime('%H:%M:%S'),  #library: Key Value Pairs
    "date":datetime.date.today()
    }
    if 'run' not in request.session:
        request.session['run'] = 1
    if request.session['run'] > 0:
        request.session['new_word'] = RandomWords().random_word()
    if 'sum' not in request.session:
        request.session['sum'] = 0

    return render(request,
    'vinmyMVC/index.html', context)

def show(request):
    print(request.method)
    return render(request,
    'vinmyMVC/show_users.html')

def aboutme(request):
    print(request.method)
    return render(request,
    'vinmyMVC/aboutme.html')

def projects(request):
    print(request.method)
    return render(request,
    'vinmyMVC/projects.html')

def create(request):
    print(request.method)
    if request.method == "POST":
        print ('*'*50)
        print(request.POST)
        print ('*'*50)
        request.session['name'] = request.POST['first_name']
        request.session['comment'] = request.POST['comment']
        request.session['cartype'] = request.POST['cartype']
        request.session['genretype'] = request.POST['genretype']

        return redirect('/users')
    else:
        return redirect('/')
def gen(request):
	if request.method == 'POST':
		request.session['run'] += 1
	return redirect('/')
def back(request):
    if request.method == 'POST':
        return redirect('/')


def all(request):
    if request.method == 'POST':
        if 'activity' not in request.session:
            request.session['activity'] = ''
        if request.POST['location'] == 'farm':
            gold_earned = random.randrange(10,21)
    	    request.session['sum'] += gold_earned
        if request.POST['location'] == 'cave':
            gold_earned = random.randrange(5,11)
    	    request.session['sum'] += gold_earned
        if request.POST['location'] == 'house':
            gold_earned = random.randrange(2,6)
    	    request.session['sum'] += gold_earned
        if request.POST['location'] == 'casino':
            gold_earned = random.randrange(-50,51)
    	    request.session['sum'] += gold_earned
        if gold_earned >= 0:
            request.session['activity'] += 'Earned {} from {} \n'.format(gold_earned, request.POST['location'])
        #
        # else:
		# 	request.session['activity'] += 'Lost {} from {}. Unlucky! \n'.format(gold_earned, request.POST['location'])
        return redirect('/')
# def farm(request):
#     if request.method == 'POST':
#         gold_earned = random.randrange(10,21)
#     	request.session['sum'] += gold_earned
#         return redirect('/')
# def cave(request):
#     if request.method == 'POST':
#         gold_earned = random.randrange(5,11)
#     	request.session['sum'] += gold_earned
#         return redirect('/')
# def house(request):
#     if request.method == 'POST':
#         gold_earned = random.randrange(2,6)
#     	request.session['sum'] += gold_earned
#         print random.randrange(2,6)
#         return redirect('/')
# def casino(request):
#     if request.method == 'POST':
#         gold_earned = random.randrange(-50,51)
#     	request.session['sum'] += gold_earned
#         return redirect('/')

# Create your views here.

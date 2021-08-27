from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . models import  Question
from django.template import loader
from django.shortcuts import render

def index(request):
    latest_question_list =Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You are looking at question %s" % question_id)

def results(request, question_id):
    response = "You are looking the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

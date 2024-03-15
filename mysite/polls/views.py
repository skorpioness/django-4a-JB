from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def counter(request):
    text_file = open("./templates/counter.html", "r")
    page = text_file.read()
    text_file.close()
    return HttpResponse(page)
def basic(request):
    text_file = open("./templates/basic.html", "r")
    page = text_file.read()
    text_file.close()
    return HttpResponse(page)
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})